from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('question/', include('question.urls')),
    path('manager/', include('manager.urls')),
    path('', include('main.urls')),
    path('apply/', include('apply.urls')),
]