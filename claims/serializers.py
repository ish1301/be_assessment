from rest_framework import serializers

from claims.models import Claim

class ClaimSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Claim
        fields = ['id']
