from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def index(request):
    return render(request, 'index.html')