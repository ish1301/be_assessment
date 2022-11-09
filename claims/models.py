from django.db import models


class Claim(models.Model):
    provider_fees = models.CharField(unique=True, max_length=150)
    member_coinsurance = models.CharField(max_length=255, blank=True, null=True)
    member_copay = models.CharField(max_length=20, blank=True, null=True)
    allowed_fees = models.CharField(max_length=255, blank=True, null=True)
