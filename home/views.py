from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def Act_list(request):
    return render (request, 'Act_list.html')