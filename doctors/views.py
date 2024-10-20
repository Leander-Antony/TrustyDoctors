from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from django.http import JsonResponse
import json

# Create your views here.

def home(request):
    return render(request, 'index.html')

def all_doctors(request):
    return render(request, 'doctors.html')


def appointment_view(request):

    # # Handle GET request to render the appointment page
    return render(request, 'appion.html', {})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords are not the same')
            return redirect('register')
    else:
        return render(request, 'create.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login_view')
    else:
        return render(request, 'login.html')
