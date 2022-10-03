from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def home(request):
    # context = {
    #     'Params' : 'I am from variable'
    # }
    return render(request, 'index.html' )

def Act_list(request):
    return render (request, 'Act_list.html')

def Login(request):
    return render (request,'Login.html')

def Employees(request):
    return render (request, 'Employees.html')

def Assignments(request):
    return render (request, 'Assignment.html')