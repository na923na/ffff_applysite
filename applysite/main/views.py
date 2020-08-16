from django.shortcuts import render, redirect

# Create your views here.
def layout(request):
    return render(request, 'layout/layout.html')

def about(request):
    return render(request, 'about/about.html')

def home(request):
    return render(request, 'home/home.html')

def logout(request):
    request.session.modified =True
    del request.session["user"]
    return redirect ('home')

