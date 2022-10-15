#from multiprocessing import context

from django.shortcuts import render
from .models import Index, ActivityList


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Index
# Create your views here.
def home(request):
    all_employees = Index.objects.all()
    return render(request, 'index.html', { 'all_employees': all_employees } )

def Act_list(request):
    activity_List = ActivityList.objects.all()
    return render (request, 'Act_list.html' , {'activity_list': activity_List})

def login(request):

    if request.method == 'POST':         
        username = request.POST['username']
        password = request.POST['password']
    
        
        user = authenticate( request, username=username, password=password)
        if user is not None :
            login( request, user )  
            return redirect('/home')            
        else:
            messages.error( request , 'Wrong username or password') 

    return render (request,'login.html')

def Employees(request):
    return render (request, 'Employees.html')

def Assignments(request):
    return render (request, 'Assignment.html')