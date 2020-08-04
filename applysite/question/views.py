from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from user.models import CustomUser

def question_update(request, pk): #선주가 한 거 ^o^! 
    if request.method == 'POST': 
        title = request.POST['title'] 
        question = request.POST['question']
        qna = Question.objects.get(pk=pk)
        qna.title = title
        qna.content = content
        qna.save()
        return redirect('home') 

    else:
        qna = get_object_or_404(Question, pk=pk)
        context = {"qna" : qna}
        return render(request, 'question/update.html', context)

def question_delete(request, pk): #선주
    qna = Question.objects.get(pk=pk)
    qna.delete()
    return redirect('question_read') #이름 맞춰야 함!
