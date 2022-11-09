import csv
from rest_framework import serializers
from rest_framework.serializers import FileField

from claims.models import Claim

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = ['unique_id', 'provider_fees', 'member_coinsurance']

class ClaimFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = ['filename']

    def validate_filename(self, value):
        """
        Validate CSV file for integrity and return true
        """

        raise serializers.ValidationError("Invalid file")

    def create(self, validated_data):
        """
        Create claims as you have already validated data upto here
        """
        pass