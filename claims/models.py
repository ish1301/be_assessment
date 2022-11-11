import uuid
from django.db import models


class Claim(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    filename = models.FileField(upload_to='./uploads/', blank=True, null=True)
    provider_fees = models.CharField(max_length=255, blank=True, null=True)
    member_coinsurance = models.CharField(max_length=255, blank=True, null=True)
    member_copay = models.CharField(max_length=20, blank=True, null=True)
    allowed_fees = models.CharField(max_length=255, blank=True, null=True)

    @property
    def net_fee(self):
        fees = (self.provider_fees + self.member_coinsurance + self.member_copay - self.allowed_fees)
        return fees if fees > 0 else 0


    """
    Process payment with 3rd party and return boolean 
    """
    def process_payment(self):
        if self.net_fee == 0:
            # process payment with payment gateway
            # or raise error upon failure
            return True

        return True

    def __str__(self) -> str:
        return str(self.unique_id)