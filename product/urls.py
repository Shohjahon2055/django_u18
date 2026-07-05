from django.urls import path

from product.views import index_list, create_category, create_product

urlpatterns=[
    path('',index_list,name='index'),
    path('cat/create/',create_category,name='category'),
    path('product/create/',create_product,name='product'),
]