from rest_framework import serializers
from rest_framework.serializers import FileField

from claims.models import Claim

class ClaimSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    file = FileField()

    class Meta:
        model = Claim
        fields = ['id', 'provider_fees', 'member_coinsurance']

class ClaimFormSerializer(serializers.ModelSerializer):
    file = FileField()

    class Meta:
        model = Claim
        fields = ['file']
