from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update', views.cart_update, name='cart_update')
]