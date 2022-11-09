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
        Check that the blog post is about Django.
        """
        raise serializers.ValidationError("Invalid file")
