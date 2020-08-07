from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from .models import CustomUser


def sign_up(request):
    if request.method =='POST':
        username = request.POST['username']
        class_code = request.POST['class_code']
        major = request.POST['major']
        phone_number = request.POST['phone_number']  #추가내용
        email = request.POST['email']  #추가내용
        pwd = request.POST['password']
        c_pwd = request.POST['check_password']


        if CustomUser.objects.filter(email=email).distinct():
            return render(request, 'user/sign_up.html', {'err' : '중복 아이디가 존재합니다.'})
            if pwd != c_pwd:
                return render(request, 'user/sign_up.html', {'err' : '암호는 서로 일치해야 합니다.'})
        customUser = CustomUser(
            username = username,
            email = email,
            major = major,
            phone_number = phone_number,
            class_code = class_code,
            )
        customUser.set_password(pwd)
        customUser.save()
        return render(request, 'user/login.html') #return redirect('home')
    else:
        return render(request, 'user/sign_up.html')

def login(request):
    if request.method == "POST" :
        email = request.POST['email']
        pwd = request.POST['password']

        user = get_object_or_404(CustomUser, email= email)
        if check_password(pwd, user.password):
            request.session['user'] = user.username
            return redirect('home')
        else:
            return render(request, 'user/login.html', {'err' : '비밀번호가 틀렸습니다...'})
    
    else:
        return render(request, 'user/login.html')

def logout(request):
    if request.session.get('user', False) :
        request.session.modified = True
        del request.session['user']
        return redirect("home")
    else:
        return redirect("home")
        
def manager_login(request): #선주
    if request.method == "POST":
        email =ruequest.POST['email']
        pwd = request.POST['password']
        is_manager = get_object_or_404(CustomUser, email=email)
        if check_password(pwd, is_manager.password):
            request.session['is_manager'] = is_manager.username
            return render(request, 'manager/manager.html')
        else:
            return render(request, 'user/manager_login.html') #아직 홈 없어서 임시로 로그인 페이지로 넘어가게 해뒀습니당 -선주
            
           
            if is_manager.is_staff : #is_staff 함수 사용
                request.session['is_manager'] = True #로그인 된다면
                return render(request, 'manager/manager.html')
            else: #로그인 안 될 시
                return render(request, 'user.login.html')                    

def manager_logout(request): #선주 
    if request.session.get('is_manager', False):
        request.session.modified= True
        del request.session['is_manager']
        return redirect("login") #임시
    else:
        return redirect("login") #임시





'''def manager_login(request): #종인
    if request.method == "POST":
        email =request.POST['email']
        pwd = request.POST['password']        
        
        user = authenticate(request, email=email, password = pwd) #종인
        if user is not None:
            login(request, user)
            return render(request, 'manager/manager.html')
        else: 
            return render(request, 'user/login.html')

def manager_logout(request):
    logout(request) 
    return redirect('home')'''

        
        
        
     

'''def manager_login(request): #선주
    if request.method == "POST":
        email =request.POST['email']
        pwd = request.POST['password']
        is_manager = get_object_or_404(CustomUser, email=email)
        if check_password(pwd, is_manager.password):
            request.session['is_manager'] = is_manager.username
            return render(request, 'manager/manager.html')
        else:
            return render(request, 'user/login.html') #아직 홈 없어서 임시로 로그인 페이지로 넘어가게 해뒀습니당 -선주'''

