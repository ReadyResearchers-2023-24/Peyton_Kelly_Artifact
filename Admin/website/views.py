from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

import os

# Create your views here.


# Imaginary function to handle an uploaded file.


def home(request):

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
            if form.is_valid():

                form.save()
                messages.success(request, "Record updated successfully!")
                return redirect("home")
        return render(request, "edit_record.html", {"form": form})
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
