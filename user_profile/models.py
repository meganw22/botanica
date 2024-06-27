from django.contrib.auth.models import User
from django.db import models


class Address(models.Model):
    """
    Model to store address details.
    """
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return f"{self.street_address1}, {self.town_or_city}, {self.country}"


class UserProfile(models.Model):
    """
    Model to store user profile details.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_address = models.OneToOneField(
        Address, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username
