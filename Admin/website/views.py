from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

import os
import time
import psutil
import requests
from datetime import datetime
from .models import Monitor
from urllib.parse import urlparse
from django.core.paginator import Paginator

# Create your views here.





def home(request):
    # get the IP address of the user
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    response = requests.get('http://api.ipstack.com/'+ip+'?access_key=7ff9f8d117530b7a7a4ffaee163f1d55') #change from HTTP to HTTPS on the IPSTACK API if you have a premium account
    rawData = response.json()
    print(rawData) # print this out to look at the response
    continent = rawData['continent_name']
    country = rawData['country_name']
    capital = rawData['city']
    city = rawData['location']['capital']
    now = datetime.now()
    datetimenow = now.strftime("%Y-%m-%d")
    saveNow = Monitor(
        continent=continent,
        country=country,
        capital=capital,
        city=city,
        datetime=datetimenow,
        ip=ip
    )
    saveNow.save()
    
    

    records = Record.objects.all()
    
    # check if logging in
    if request.method == "POST":
        # attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        # authenticate user
        
        user = authenticate(request, username=username, password=password)
        # check if authentication successful
        if user is not None:
            login(request, user)
            
            messages.success(request, f"You have logged in, {username}!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.try again.")
            return redirect("home")
    else:
        
        return render(request, "home.html", {"records": records})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")

    return redirect("home")


def register_user(request):
    if request.method == "POST":
        
        
        form = SignUpForm(request.POST)
        if form.is_valid():
            
            form.save()
            # store IP address of user
            
            # create a new record object

            # authenticate user / login user
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)
            # check if authentication successful

            login(request, user)
            messages.success(request, f"Account created successfully!")
            return redirect("home")

    else:
        form = SignUpForm()

        return render(request, "register.html", {"form": form})
    return render(request, "register.html", {"form": form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # look up the record
        customer_record = Record.objects.get(id=pk)
        return render(request, "record.html", {"customer_record": customer_record})
    else:
        messages.success(request, "Please login to view this page.")
        return redirect("home")


def delete_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        customer_record.delete()
        # remove the file path
        for filename in os.listdir("media/"):
            if filename == customer_record.file:
                os.remove("media/uploads" + filename)

        messages.success(request, "Record deleted successfully!")
        return redirect("home")
    else:
        messages.success(request, "Please login to view this page.")
        return redirect("home")


def add_record(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddRecordForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("home")
            else:
                context["form"] = form
                return render(request, "upload.html", context)
        context = {"form": AddRecordForm()}
        return render(request, "upload.html", context)
    else:
        messages.success(request, "Please login to view this page.")
        return redirect("home")


def handle_uploaded_file(f):
    with open("some/file/name.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def edit_record(request, pk):

    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(
            request.POST, request.FILES or None, instance=current_record
        )
        if request.method == "POST":
            form = AddRecordForm(
            request.POST, request.FILES or None, instance=current_record
        )
            if form.is_valid():
                
                form.save()
                messages.success(request, "Record updated successfully!")
                return redirect("home")
        return render(request, "edit_record.html", {"form": form},)
    else:
        messages.success(request, "Please login to view this page.")
        return redirect("home")


def upload(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddRecordForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("home")
            else:
                context["form"] = form
                return render(request, "upload.html", context)
        context = {"form": AddRecordForm()}
        return render(request, "upload.html", context)
    else:
        messages.success(request, "Please login to view this page.")
        return redirect("home")

def traffic_monitor(request):
    # is authenticated as a user
    if request.user.is_authenticated:
    # Getting loadover15 minutes
        dataSaved = Monitor.objects.all().order_by('-datetime')
        # Getting loadover15 minutes 
        load1, load5, load15 = psutil.getloadavg()
        cpu_usage = int((load15/os.cpu_count()) * 100)
        ram_usage = int(psutil.virtual_memory()[2])
        p = Paginator(dataSaved, 100)
        #shows number of items in page
        totalSiteVisits = (p.count)
        #find unique page viewers & Duration
        pageNum = request.GET.get('page', 1)
        page1 = p.page(pageNum)
        #unique page viewers
        a = Monitor.objects.order_by().values('ip').distinct()
        pp = Paginator(a, 10)
        #shows number of items in page
        unique = (pp.count)
        #update time
        now = datetime.now()
        data = {
            "now":now,
            "unique":unique,
            "totalSiteVisits":totalSiteVisits,
            "cpu_usage": cpu_usage,
            "ram_usage": ram_usage,
            "dataSaved": page1,
        }
        return render(request, 'monitor.html', data)
    else:
        messages.success(request, "Please login to view this page.")
        return redirect("home")


