from django.shortcuts import render, redirect

def index(request):
    return redirect('/')

def home(request):  
    return render(request, 'home.html')