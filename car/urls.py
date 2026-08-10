from django.urls import path
from car import views

urlpatterns = [
    path('', views.get_cars, name='list'),
    path('create/', views.create_car, name='create'),
    path('detail/<int:pk>/', views.detail_car, name='detail'),
    path('edit/<int:pk>/', views.edit_car, name='edit_car'),
    path('delete/<int:pk>/', views.delete_car, name='delete_car'),
    path('create_phone/', views.create_phone, name='create_phone'),

    path('about/list/', views.AboutListView.as_view(), name='list-about'),
    path('about/create/', views.AboutCreateView.as_view(), name='create-about'),
    path('excel/create/', views.exprort_about_to_excel, name='create-excel'),
    path('about/update/<int:pk>/', views.AboutUpdateView.as_view(), name='update-about'),
    path('about/detail/<int:pk>/', views.AboutDetailView.as_view(), name='detail-about'),
    path('about/delete/<int:pk>/', views.AboutDeleteView.as_view(), name='delete-about'),

    path('post/<int:post_id>/like/', views.toggle_like, name='toggle_like'),
]