from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import VerificationToken
import uuid

from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, is_active=True)
                # create verification token
                token = uuid.uuid4().hex
                VerificationToken.objects.create(user=user, token=token, verified=False)
                verify_link = request.build_absolute_uri(f"/accounts/verify/{token}/")
                # show simulated email page
                return render(request, 'accounts/check_email.html', {'verify_link': verify_link})
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # check verification
                try:
                    token = VerificationToken.objects.get(user=user)
                    if not token.verified:
                        messages.error(request, 'Account not verified. Check the verification link.')
                        return redirect('accounts:login')
                except VerificationToken.DoesNotExist:
                    pass
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def verify(request, token):
    try:
        vt = VerificationToken.objects.get(token=token)
        vt.verified = True
        vt.save()
        return render(request, 'accounts/verified.html', {'user': vt.user})
    except VerificationToken.DoesNotExist:
        return render(request, 'accounts/verify_failed.html')
