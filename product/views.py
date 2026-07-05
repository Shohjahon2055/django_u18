from django.shortcuts import render,redirect

from .forms import CategoryForm, ProductForm
from .models import Product, Category


# Create your views here.

def index_list(request):
    categories=Category.objects.all()
    products=Product.objects.all()
    context={
        'products':products,
        'categories':categories

    }
    return render(request,'product/index.html',context)


def create_category(request):
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form=CategoryForm()
    return render(request,'product/category_create.html',{'form':form})


def create_product(request):
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form=ProductForm()
    return render(request,'product/product_create.html',{'form':form})
