import openpyxl
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from openpyxl import workbook

from .models import About, Like

from .forms import AboutForm
from django.urls import reverse_lazy
from django.http import HttpResponse

from accounts.permissions import login_required, check_admin, check_manager, check_manager_or_admin
from car.forms import CarForm, PhoneForm, CarEditForm
from car.models import Car, Phone
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


@login_required
def toggle_like(request, post_id):
    about = get_object_or_404(About, id=post_id)
    user = request.user

    like, created = Like.objects.get_or_create(
        user=user,
        about=about
    )

    if created:
        about.likes.add(user)

    else:
        about.likes.remove(user)

    return redirect("detail-about", pk=about.pk)


def get_about(request, pk):
    about = About.objects.get(pk=pk)
    context = {
        'about': about,
    }
    return render(request, 'about/detail.html', context)


# Create your views here.

def get_cars(request):
    cars = Car.objects.all()
    phones = Phone.objects.all()
    context = {
        'cars': cars,
        'phones': phones,
    }
    return render(request, 'car/list.html', context)


@check_admin
def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form = CarForm()

    context = {
        'form': form
    }
    return render(request, 'car/create.html', context)


def create_phone(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form = PhoneForm()

        context = {
            'form': form
        }

        return render(request, 'car/create_phone.html', context)


@login_required
def detail_car(request, pk):
    car = Car.objects.get(pk=pk)
    context = {
        "car": car
    }
    return render(request, "car/detail.html", context)


@check_manager_or_admin
def edit_car(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        form = CarEditForm(request.POST, instance=car)

        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form = CarEditForm(instance=car)

    return render(request, 'car/create.html', {"form": form})


@check_admin
def delete_car(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        car.delete()
        return redirect("list")
    else:
        return render(request, 'car/delete.html', {"car": car})


class AboutListView(ListView):
    model = About
    template_name = 'about/list.html'
    context_object_name = 'abouts'


class AboutDetailView(DetailView):
    model = About
    template_name = "about/detail.html"
    context_object_name = "about"
    pk_url_kwarg = 'pk'


class AboutCreateView(CreateView):
    form_class = AboutForm
    template_name = 'about/create.html'
    success_url = reverse_lazy("list-about")
    context_object_name = 'form'


class AboutUpdateView(UpdateView):
    model = About
    form_class = AboutForm
    template_name = 'about/create.html'
    success_url = reverse_lazy("list-about")
    context_object_name = 'form'
    pk_url_kwarg = 'pk'


class AboutDeleteView(DeleteView):
    model = About
    template_name = 'about/delete.html'
    success_url = reverse_lazy("list-about")
    pk_url_kwarg = 'pk'
    context_object_name = 'about'


# excel

def exprort_about_to_excel(request):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "About"

    sheet.append([
        'ID',
        'Title',
        'Description',
    ])

    for about in About.objects.all():
        sheet.append([
            about.id,
            about.title,
            about.description,
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    response['Content-Disposition'] = 'attachment; filename="About_Excel.xlsx"'

    workbook.save(response)

    return response