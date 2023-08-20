from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    CHOICES = (
        (1, 'admin'),
        (2, 'user')
    )
    phone = PhoneNumberField(region="UZ", default='')
    roles = models.PositiveSmallIntegerField(default=1, choices=CHOICES)
