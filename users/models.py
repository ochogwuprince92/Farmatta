from django.db import models
from django.contrib.auth.models import AbstractUser

# Define a class for the users
class CustomUser(AbstractUser):
    is_farmer = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null= False, blank=False)