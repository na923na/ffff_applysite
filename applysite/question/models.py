from django.db import models
from user.models import CustomUser
from django.utils import timezone

class Question(models.Model) :

    author = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    title = models.CharField(max_length=40)
    question = models.TextField()
    question_time = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title

class Answer(models.Model) :
    author = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE) #각 질문에 맞는 답을 해야하기 때문에 추가함 (최종인)
    answer  = models.TextField()
    answer_time = models.DateTimeField(default=timezone.now)
    
    
    

    def __str__(self) :
        return self.answer