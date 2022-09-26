from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('' , views.home, name='home'),
   path('Activity_list',views.Act_list, name='Activity_list')
]