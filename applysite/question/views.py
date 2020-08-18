from django.shortcuts import render, get_object_or_404, redirect
from question.models import Question
from manager.models import Manager
from user.models import CustomUser

def question_update(request, pk): #선주가 한 거 ^o^! 
    if request.method == 'POST': 
        title = request.POST['title'] 
        content = request.POST['content']
        qna = Question.objects.get(pk=pk)
        qna.title = title
        qna.content = content
        
        qna.save()
        return redirect('question_read') 

    else:
        qna = get_object_or_404(Question, pk=pk)
        context = {"qna" : qna}
        return render(request, 'question/update.html', context)

# def update(request):
#     return render(request, 'question/update/html')

def question_delete(request, pk): #선주
    qna = Question.objects.get(pk=pk)
    qna.delete()
    return redirect('question_read') #이름 맞춰야 함!


def question_read(request): #(최종인)
    questions = Question.objects.all() #question에 있는 객체들을 다 불러온다
    context = {'questions' : questions } # ''안에있는건 내가 정의한거: question's' 인이유는 read에서 모든 게시물들을 보니깐 
    return render(request, 'question/read.html', context)

def question_read_one(request, pk): #(최종인)
    question = get_object_or_404(Question, pk = pk) 
    context = {'question' : question }  #question's'가 아닌이유는 read_one에서 개별 항목에 대한 것을 볼것이기 때문
    
    
    return render(request, 'question/read_one.html', context) 
def question_viewanswer(request, pk): #종인/질문+답변 동시 확인/미완성 
     question = get_object_or_404(Question, pk = pk)
     manager = get_object_or_404(Manager, question = question)
     context = {'question' : question, 'manager' : manager}

     return render(request, 'question/viewanswer.html', context)

def question_create(request):
    if request.method == 'POST' and request.session.get('user', False): #로그인해야 기능 이용 가능 
        title = request.POST['title']
        author = get_object_or_404(CustomUser, username = request.session['user'])
        content = request.POST['content']
        
        question = Question(
            title = title,
            author = author,
            content = content,            
        )
        question.save()

        return redirect('question_read')
    else:
        return render(request, 'question/create.html') 

def pre_update(request, pk):
    question = Question.objects.get(pk=pk)
    context = {'question': question}
    return render(request, "question/update.html", context)

