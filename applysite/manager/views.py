from django.shortcuts import render, get_object_or_404, redirect
from question.models import Question
from manager.models import Manager
from user.models import CustomUser

def manager_read(request):
    managers = Manager.objects.all()
    context = {'managers': managers}
    return render(request, 'manager/manager_read.html', context)

def manager_read_one(request, pk):
    manager = get_object_or_404(Manager, pk=pk)
    context = {'manager': manager}
    return render(request, 'manager/manager_read_one.html', context)

def manager_create(request):
    if request.method == 'POST' and request.session.get('is_manager', False): #로그인해야 기능 이용 가능 
        question = request.POST['question']
        question_value = Question.objects.get(pk = question)
        author = get_object_or_404(CustomUser, username = request.session['is_manager'])
        content = request.POST['content']
        manager = Manager(
            author = author,
            question = question_value,
            content = content,            
        )

        manager.save()

        return redirect('manager_read')
    else:
        question_pk = request.GET['question']
        return render(request, 'manager/manager_create.html', {'question' : question_pk})    


def manager_update(request, pk): 

    if  request.method == 'POST':
        #question = request.POST['question']
        # author = request.POST['author']
        # Cuser = CustomUser.objects.get(username=author) #커스텀유저 안에서 author라는 이름을 가진 객체를 가져오는것 
        content = request.POST['content']
        manager = Manager.objects.get(pk=pk)
        #manager.question = question
        #manager.author = Cuser
        manager.content= content
        manager.save() 

        return redirect('manager_read')
    
    else:
        manager = get_object_or_404(Manager, pk=pk)
        context = {"manager":manager}

        return render(request, 'manager/manager_update.html', context)
def manager_pre_update(request, pk):
    manager = Manager.objects.get(pk=pk)
    context = {'manager':manager}
    return render(request, "manager/manager_update.html", context)

def manager_delete(request, pk): 
    manager = Manager.objects.get(pk=pk)
    manager.delete()
    return redirect('manager_read')      

def manager_home(request):
    return render(request, 'manager/manager_home.html')



