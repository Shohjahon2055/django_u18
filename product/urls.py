from django.urls import path

from product.views import index_list, create_category

urlpatterns=[
    path('',index_list,name='index'),
    path('cat/create/',create_category,name='category'),
]