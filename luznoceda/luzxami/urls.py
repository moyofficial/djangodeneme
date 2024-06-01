from django.contrib import admin
from django.urls import path
from django.urls import re_path
from luzxami import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', views.luz, name='amity'),
    re_path('youtube/', views.youtube, name='luz'),
    ]