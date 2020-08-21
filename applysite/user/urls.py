from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('sign_up/', views.sign_up, name = 'sign_up'),
    path('logout/', views.logout, name='logout'),
    path('manager_login/', views.manager_login, name="manager_login"),
    path('manager_logout/', views.manager_logout, name="manager_logout"),
]