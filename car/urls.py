from django.urls import path

from car import views

urlpatterns=[
    path('',views.get_cars,name='list'),
    path('create/',views.create_car,name='create'),
    path('create_phone/',views.create_phone,name='create_phone'),
]