from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=10, null=True, blank=True) 
    birth_day = models.DateField(default=timezone.now, null=True, blank=True)
