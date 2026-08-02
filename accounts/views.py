from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate,login
from .forms import LoginForm, RoleForm, ForgetPasswordForm

from accounts.forms import RegisterForm
from .models import CustomUser
from .utils import send_simple_email
from .utils import send_html_email


# Create your views here.

def register_user(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data.get('password')
            user=form.save()
            user=authenticate(username=user.username,password=password)
            if user:
                username=user.username
                user_email=user.email
                # send_simple_email(user_email)
                send_html_email(user_email,username)
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




# role berish

def role_change(request):
    if request.method=='POST':
        form=RoleForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            role=form.cleaned_data.get('role')
            user=CustomUser.objects.filter(username=username.username).first()
            if user:
                user.role=role
                user.save()
                return redirect("list")
    else:
        form=RoleForm()
    return render(request,"accounts/role.html",{'form':form})



def forget_password_post(request):
    if request.method=='POST':
        form=ForgetPasswordForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')


    form=ForgetPasswordForm()
    return render(request,'accounts/forget.html',{'form':form})