from django.urls import path

from product.views import index_list

urlpatterns=[
    path('',index_list,name='index')
]