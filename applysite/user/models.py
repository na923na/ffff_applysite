from django.db import models
from django.contrib.auth.models import AbstractUser 

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length = 12, null = True, blank = True)
    class_code = models.CharField(max_length = 9, null = True, blank = True)
    major = models.CharField(max_length = 15, null = True, blank = True)
    

