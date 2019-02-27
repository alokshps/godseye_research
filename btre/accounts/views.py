from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def login(request):
     return render (request, 'accounts/login.html')


def register(request):
     if request.method == 'POST':
          messages.error(request, 'Testing Error Message')
          return redirect('register')
     else: 
          return render (request, 'accounts/register.html')

def logout(request):
     return redirect ('index')