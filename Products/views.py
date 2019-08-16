from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from cart.models import Cart

# Create your views here.

#View for all Products
def index(request):
    
    products = Product.objects.order_by('-list_date')
    context = {
        'products': products
    }
    return render (request, 'products/index.html', context)


#View for a Single Product
def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    context = {
        'product': product,
        'cart': cart_obj
    }
    return render(request, 'products/product.html',context)

#View for Featured Products
def featured(request):
    featured_products = Product.objects.order_by('-list_date').filter(featured=True)
    
    context = {
        'featured_products' : featured_products
    }
    print (featured_products)
    return render(request, 'products/featured.html', context)



#Views to search for Products
def search(request):
    queryset_list = Product.objects.order_by('-list_date')
    
    #search by name of products
    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            #search by different fields inside the products models
            lookup = Q(name__icontains = name) | Q(description__icontains = name)
            queryset_list = queryset_list.filter(lookup).distinct()

    context = {
       
        'products': queryset_list,
        'values': request.GET,
    }   
    return render(request, 'products/search.html', context)