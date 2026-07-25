from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate

from accounts.forms import RegisterForm


# Create your views here.

def register_user(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data.get('password')
            user=form.save()
            user=authenticate(username=user.username,password=password)
            if user:
                login(request,user)
                return redirect('list')
            return redirect('list')
    else:
        form=RegisterForm()
    return render(request,'accounts/register.html',{'form':form})


def login_view(ruquest):
    if ruquest.method=='POST':
        form=LoginForm(data=ruquest.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user:
                login(ruquest,user)
                return redirect("list")

    else:
        form=LoginForm()
    return render(ruquest,'accounts/login.html',{"form":form})


def logout_view(request):
    logout(request)
    return redirect("login")
