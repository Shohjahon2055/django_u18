from django.shortcuts import render
from .models import Product, Category

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    query = request.GET.get('q')
    category_id = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    available = request.GET.get('available')

    if query:
        products = products.filter(name__icontains=query)

    if category_id:
        products = products.filter(category_id=category_id)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    if available == 'true':
        products = products.filter(is_available=True)
    elif available == 'false':
        products = products.filter(is_available=False)

    context = {
        'products': products,
        'categories': categories,
        'query': query,
        'selected_category': category_id,
        'min_price': min_price,
        'max_price': max_price,
        'available': available,
    }

    return render(request, 'product/product.html', context)