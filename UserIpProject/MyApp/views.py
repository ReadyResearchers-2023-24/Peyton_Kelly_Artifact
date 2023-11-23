from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from .models import UserIp, UserIpLocation
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create Register view 
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST('username')
        email = request.POST('email')
        password = request.POST('password')
        password2 = request.POST('password2')
        if password == password2:
            if User.object.filter(email=email).exists():
                messages.info(request, 'Email already in use.')
                return redirect('register')
            elif User.object.filter(username=username).exists():
                messages.info(request, 'Username already in use.')
                return redirect('register')
            else:
                user = User.object.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
            
        else:
            messages.info(request, 'Passwords do not match.')
            return redirect('register')
        
    else:
        return render(request, 'register.html')


