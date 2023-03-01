import csv
import io

from rest_framework import serializers

from claims.models import Claim


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = ['unique_id', 'provider_fees', 'member_coinsurance']

    def validate_member_coinsurance(self, value):
        if value == '$16.25':
            raise serializers.ValidationError('Invalid member coinsurance')


class ClaimFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = ['filename']

    def validate(self, data):
        """
        Validate CSV file for integrity and return validated data
        """
        decoded_file = data['filename'].read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)
        headers = [self.clean_label(i) for i in next(reader)]
        rows = []
        for row in reader:
            rows.append(self.validate_claim(row, headers))

        return rows

    def clean_label(self, head):
        for i in ['\n', '#', '/']:
            head = head.replace(i, ' ').strip()

        return head.lower().replace(' ', '_')

    def validate_claim(self, data, headers):
        if len(data) != 10:
            raise serializers.ValidationError('Invalid file')
        return {i: j for i, j in zip(headers, data)}

    def save(self):
        rows = []
        
        for row in self.validated_data:
            serializer = ClaimSerializer(data=row)
            if serializer.is_valid():
                serializer.save()
                rows.append(serializer.data)
            else:
                raise serializers.ValidationError({'message': 'Validation failed', 'errors': serializer.errors})
