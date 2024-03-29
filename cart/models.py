from django.conf import settings

from django.db import models
from datetime import datetime
from Products.models import Product
from django.db.models.signals import pre_save, post_save, m2m_changed

User = settings.AUTH_USER_MODEL
# Create your models here.

class CartManager(models.Manager):
    
    def new_or_get(self, request):
        cart_id     = request.session.get('cart_id', None)
        qs          = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        
        user_obj = None
        if user is not None:
            # try:
            #     user_is_authenticated = request.user.is_authenticated()
            # except TypeError:
            #     user_is_authenticated = request.user.is_authenticated
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)
            
class Cart(models.Model):
    user        = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    products    = models.ManyToManyField(Product, blank= True)
    total       = models.DecimalField(max_digits=20, decimal_places=2, default=00.00)
    subtotal    = models.DecimalField(max_digits=20, decimal_places=2, default=00.00)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    objects     = CartManager()

    def __str__(self):
        return str(self.id)


def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products    = instance.products.all()
        total       = 0
        for item in products:
            total += item.price
        if instance.subtotal != total:
            instance.subtotal  = total
            instance.save()

m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    instance.total = instance.subtotal

pre_save.connect(pre_save_cart_receiver, sender=Cart)