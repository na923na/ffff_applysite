from django.db import models
from user.models import CustomUser
from django.utils import timezone

class Question(models.Model) :

    author = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    title = models.CharField(max_length=40)
    content = models.TextField()
    question_time = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title


    