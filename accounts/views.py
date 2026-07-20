from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.

def register_user(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            return redirect('list')
    else:
        form=UserCreationForm()
    return render(request,'accounts/register.html',{'form':form})


def login_view(ruquest):
    if ruquest.method=='POST':
        form=AuthenticationForm(data=ruquest.POST)
        if form.is_valid():
            user=form.get_user()
            login(ruquest,user)
            return redirect("list")

    else:
        form=AuthenticationForm()
    return render(ruquest,'accounts/login.html',{"form":form})


def logout_view(request):
    logout(request)
    return redirect("login")
