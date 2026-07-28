from django.urls import path

from car import views

urlpatterns=[
    path('',views.get_cars,name='list'),
    path('create/',views.create_car,name='create'),
    path('detail/<int:pk>/',views.detail_car,name='detail'),
    path('edit/<int:pk>/',views.edit_car,name='edit_car'),
    path('delete/<int:pk>/',views.delete_car,name='delete_car'),
    path('create_phone/',views.create_phone,name='create_phone'),
]