from django.http import HttpResponse
from django.shortcuts import redirect

from accounts.models import Role


def login_required(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        return func(request,*args,**kwargs)
    return wrapper


# admin check

def check_admin(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            if not request.user.role==Role.ADMIN:
                return HttpResponse("Sizga ruxsat yo'q")
        return func(request,*args,**kwargs)
    return wrapper

# check manage

def check_manager(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            if not request.user.role==Role.MANAGER:
                return HttpResponse("Sizga ruxsat yo'q")
        return func(request,*args,**kwargs)
    return wrapper


def check_manager_or_admin(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            if ( request.user.role==Role.MANAGER) or ( request.user.role==Role.ADMIN):
                return func(request, *args, **kwargs)

            return HttpResponse("Sizga ruxsat yo'q")
        return func(request,*args,**kwargs)
    return wrapper