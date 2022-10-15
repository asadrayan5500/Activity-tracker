from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
   path('home' , views.home, name='home'),
   path('Act_list',views.Act_list, name='Act_list'),
   path('', views.login, name='login'),
   path('Employees', views.Employees, name='Employees'),
   path('Assignments', views.Assignments, name='Assignments')
]