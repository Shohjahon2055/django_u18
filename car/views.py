from django.shortcuts import render, redirect

from car.forms import CarForm, PhoneForm
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

