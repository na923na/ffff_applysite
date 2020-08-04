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
