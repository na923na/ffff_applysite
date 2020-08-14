from django.shortcuts import render

# Create your views here.
def layout(request):
    return render(request, 'layout/layout.html')

def about(request):
    return render(request, 'about/about.html')

def home(request):
    return render(request, 'home/home.html')
