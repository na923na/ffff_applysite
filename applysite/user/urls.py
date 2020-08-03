from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('signup/', views.sign_up, name = 'sign_up'),
]