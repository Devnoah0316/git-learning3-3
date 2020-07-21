from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def cshapi(request):
    return render(request, 'cshapi.html')

def shapi(request):
    return render(request, 'shapi.html')