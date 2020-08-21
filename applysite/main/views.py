from django.shortcuts import render, redirect

# Create your views here.
def layout(request):
    return render(request, 'layout/layout.html')

def about(request):
    return render(request, 'about/about.html')

def home(request):
    return render(request, 'home/home.html')

def email(request):
    return render(request, 'email/email.html')

# def email_create(request) :
#     if request.method == 'POST':
#         email_address = request.POST['email_address']
#         title = request.POST['title']
#         content = request.POST['content']
                                                              #모델 생성 전 작업만 해 둠 ! 만들라고 하면 url, model 작업해야 함!
#         sendemail = Email(
#             email_address = email_address,
#             title = title,
#             content = content,
#             )
#         apply.save()
#         return redirect('email_create')
#     else:
#         return render(request, 'mail/email.html')
