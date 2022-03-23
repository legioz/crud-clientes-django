from django.db import models
from apps.core import models as core_models


class Phone(models.Model):
    user = models.ForeignKey(core_models.User, on_delete=models.CASCADE)
    number = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        verbose_name = "Phone"

    def __str__(self) -> str:
        return self.number


class Address(models.Model):
    user = models.ForeignKey(core_models.User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250, blank=False, null=False)
    # TODO implementar api IBGE?

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self) -> str:
        return self.address
