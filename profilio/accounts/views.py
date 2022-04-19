from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template



def index(request):
    return render(request, 'accounts/index.html', {'title': 'index'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form, 'title': 'reqister here'})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = auth_login(request, user)
            messages.success(request, f' Welcome, {username}.')
            return redirect('index')
        else:
            messages.info(request, f'No account exist')
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form, 'title': 'log in'})