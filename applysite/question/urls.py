"""applysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [

    path('update/<int:pk>', views.question_update, name='question_update'),#선주 
    path('delete/<int:pk>', views.question_delete, name='question_delete'),#선주   
    path('read/', views.question_read, name="question_read"), #question 안에 있는 read라서 question_read라 함 (최종인)
    path('read/<int:pk>', views.question_read_one, name="question_read_one"), # question 안에 있는 read_one이라서 question_read_one 이라 함 / int:pk는 개별 게시글에 대한 것이므로 추가함 (최종인)
    path('create/', views.question_create, name="question_create"),
    path('pre_update/<int:pk>', views.pre_update, name='pre_update'),
    path('viewanswer/<int:pk>', views.question_viewanswer, name='question_viewanswer'),

]
