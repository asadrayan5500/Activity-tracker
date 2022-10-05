from multiprocessing import context

from django.shortcuts import render
from .models import Index, ActivityList


# Create your views here.
def home(request):
    all_employees = Index.objects.all()
    return render(request, 'index.html', { 'all_employees': all_employees } )

def Act_list(request):
    return render (request, 'Act_list.html')

def Login(request):
    return render (request,'Login.html')

def Employees(request):
    return render (request, 'Employees.html')

def Assignments(request):
    return render (request, 'Assignment.html')