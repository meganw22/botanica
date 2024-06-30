from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


class Address(models.Model):
    """
    Model to store address details.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='addresses',
        null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)

    def __str__(self):
        return f"{self.street_address1}, {self.town_or_city}, {self.country}"


class UserProfile(models.Model):
    """
    Model to store user profile details.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
