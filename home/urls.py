from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('' , views.home, name='home'),
   path('Act_list',views.Act_list, name='Act_list'),
   path('Login', views.Login, name='Login'),
   path('Employees', views.Employees, name='Employees'),
   path('Assignments', views.Assignments, name='Assignments')
]