from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.apply_create, name = 'apply_create'),
    path('read/', views.apply_read, name = 'apply_read'),
]