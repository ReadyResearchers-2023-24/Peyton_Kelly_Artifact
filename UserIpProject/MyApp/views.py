from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout


# Create Register view 
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST('username')
        email = request.POST('email')
        password = request.POST('password')
        password2 = request.POST('password2')

        if password == password2:
            if User.objects.filter(email=email).exists() or  User.objects.filter(username=username).exists():
                messages.info(request, 'Email already in use.')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful!')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match.')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST('username')
        password = request.POST('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials.')
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def IP_hidden (request):
    # Get the IP address of the user
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # If the IP address is from a proxy
        ip = x_forwarded_for.split(',')[0]
    else:
        # If the IP address is from a user
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    return render(request, 'IP_hidden.html', {'ip': ip})

