from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from .models import CustomUser

def sign_up(request):
    if request.method =='POST':
        nickname = request.POST['nickname']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        class_code = request.POST['class_code']
        major = request.POST['major']
        phone_number = request.POST['phone_number']
        pwd = request.POST['password']
        c_pwd = request.POST['check_password']
        #manager = request.POST['manager'] 관리자 로그인 
        #manager_ok = False
        #if manager == 'likelion':
        #    manager_ok=True

        if CustomUser.objects.filter(username=nickname).distinct():
            return render(request, 'user/sign_up.html', {'err1' : '중복 아이디가 존재합니다.'})
        if pwd != c_pwd:
             return render(request, 'user/sign_up.html', {'err2' : '암호는 서로 일치해야 합니다.'})

        customUser = CustomUser(
            username = nickname,
            first_name = first_name,
            last_name = last_name,
            major = major,
            phone_number = phone_number,
            class_code = class_code,
            #manager_ok = manager_ok
            )
        customUser.set_password(pwd)
        customUser.save()
        return redirect ('login')
    else:
        return render(request, 'user/sign_up.html')

def login(request):
    if request.method == "POST" :
        nickname = request.POST['nickname']
        pwd = request.POST['password']

        user = get_object_or_404(CustomUser, username = nickname)
        if check_password(pwd, user.password):
            request.session['user'] = user.username
            return render(request, 'user/login.html')  #임시로 로그인 페이지로 이동 return redirect('home')
        else:
            return render(request, 'user/login.html', {'err' : '비밀번호가 틀렸습니다...'})
    
    else:
        return render(request, 'user/login.html')
