from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from database.models import Customer
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')

    else:
        form = SignUpForm()

    return render(request, 'accounts\signup.html', {'form': form})

def user_login(request):
    print("Login view called")
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(f"User logged in: {user.username}")
            print("Redirecting to main home")
            return redirect('home')
        else:
            print("The error:", form.errors)
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

