from django.db import models
from user.models import CustomUser

class ApplyInformation(models.Model):
    reason = models.CharField(max_length = 500, null = True, blank = True)
    makeweb = models.CharField(max_length = 300, null = True, blank = True)
    solution = models.CharField(max_length = 300, null = True, blank = True)
    gain = models.CharField(max_length = 100, null = True, blank = True)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    # major = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    # class_code = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    
    

