from django.shortcuts import render, redirect
from .models import Cart
from Products.models import Product
# Create your views here.

def home(request):
    
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    # products = cart_obj.products.all()
    # total = 0
    # for item in products:
    #     total += item.price
    # cart_obj.total = total
    # cart_obj.save()
    context = {
        'cart': cart_obj
    }   
    return render (request, 'cart/home.html', context)
    # # To access all the methods available to the session method in Django
    # # print (dir(request.session))
    # request.session.set_expiry(120)
    
    # if request.session.session_key is None:
    #     return render (request, 'accounts/login.html')
    # else:
    #     return render (request, 'cart/home.html')



def cart_update(request):
    
    
    product_id = request.POST.get('product_id')
    print (product_id)
    
    if product_id is not None:
        try:
            Product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return redirect ('home')
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if Product_obj in cart_obj.products.all():
            cart_obj.products.remove(Product_obj)
        else:
            cart_obj.products.add(Product_obj)
    return redirect ('home')
