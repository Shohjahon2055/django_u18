from django.shortcuts import render,redirect

from .forms import CategoryForm
from .models import Product
# Create your views here.

def index_list(request):
    products=Product.objects.all()
    context={
        'products':products

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
