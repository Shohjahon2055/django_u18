from django.shortcuts import render
from .models import Product
# Create your views here.

def index_list(request):
    products=Product.objects.all()
    context={
        'products':products

    }
    return render(request,'product/index.html',context)