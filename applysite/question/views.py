from django.shortcuts import render

def update(request):
    return render(request, 'question/update.html')
