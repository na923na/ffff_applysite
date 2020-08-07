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
    path('manager_update/<int:pk>', views.manager_update, name='manager_update'),
    path('manager_delete/<int:pk>', views.manager_delete, name='manager_delete'),
    path('manager_read/', views.manager_read, name="manager_read"), 
    path('manager_read/<int:pk>', views.manager_read_one, name="manager_read_one"), 
    path('manager_create/', views.manager_create, name="manager_create"),
    path('manager_pre_update/<int:pk>', views.manager_pre_update, name='manager_pre_update'),
    path('manager_home', views.manager_home, name="manager_home"),

]


