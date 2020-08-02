from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.utils import timezone

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length = 12, null = True, blank = True)
    class_code = models.CharField(max_length = 9, null = True, blank = True)  

