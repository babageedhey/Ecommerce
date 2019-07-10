from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

#View for all Products
def index(request):
    
    products = Product.objects.order_by('-list_date')
    context = {
        'products': products
    }
    return render (request, 'products/index.html', context)


#View fora Single Product
def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }
    return render(request, 'products/product.html',context)


#Views to search for Products
def search(request):
    queryset_list = Product.objects.order_by('-list_date')

    return