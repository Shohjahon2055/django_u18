from django.shortcuts import render, redirect

from accounts.permissions import login_required, check_admin, check_manager,check_manager_or_admin
from car.forms import CarForm, PhoneForm,CarEditForm
from car.models import Car,Phone


# Create your views here.
def get_cars(request):
     cars=Car.objects.all()
     phones=Phone.objects.all()
     context={
         'cars':cars,
         'phones':phones,
     }
     return render(request,'car/list.html',context)


@check_admin
def create_car(request):
    if request.method=='POST':
        form=CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form=CarForm()
    context={
        'form':form
    }
    return render(request,'car/create.html',context)

def create_phone(request):
    if request.method=='POST':
        form=PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")

    else:
        form=PhoneForm()
        context={
            'form':form
        }
        return render(request,'car/create_phone.html',context)
@login_required
def detail_car(request,pk):
    car=Car.objects.get(pk=pk)
    context={
        "car":car
    }
    return render(request,"car/detail.html",context)

@check_manager_or_admin
def edit_car(request,pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = CarEditForm(request.POST,instance=car)
        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form=CarEditForm(instance=car)

    return render(request, 'car/create.html', {"form":form})
@check_admin
def delete_car(request,pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect("list")
    else:
        return render(request,'car/delete.html',{"car":car})


