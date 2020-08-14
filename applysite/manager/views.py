from django.shortcuts import render, redirect, get_object_or_404
from .models import Manager
from user.models import CustomUser

def manager_read(request):
    managers = Manager.objects.all()
    context = {'managers': managers}
    return render(request, 'manager/manager_read.html', context)

def manager_read_one(request, pk):
    manager = get_object_or_404(Manager, pk=pk) #첫번째 pk는 board안에있는 pk, 두번째 pk는 11번째 줄 pk에 대응
    context = {'manager': manager}
    return render(request, 'manager/manager_read_one.html', context)

def manager_create(request):
    if request.method == 'POST' and request.session.get('is_manager', False): #로그인해야 기능 이용 가능 
        title = request.POST['title']
        author = get_object_or_404(CustomUser, username = request.session['is_manager'])
        content = request.POST['content']
        manager = Manager(
            author = author,
            title = title,
            content = content,            
        )

        manager.save()

        return redirect('manager_read')
    else:
        return render(request, 'manager/manager_create.html')    


def manager_update(request, pk): 
    title = request.POST['title']
    author = request.POST['author']
    Cuser = CustomUser.objects.get(username=author) #커스텀유저 안에서 author라는 이름을 가진 객체를 가져오는것 
    content = request.POST['content']
    manager = Manager.objects.get(pk=pk)
    manager.title = title
    manager.author = Cuser
    manager.content = content
    manager.save() 

    return redirect('manager_read')

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



