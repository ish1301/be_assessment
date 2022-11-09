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

