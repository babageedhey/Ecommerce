from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','list_date')
    list_display_links = ('id',)
    list_filter = ('name',)
    # list_editable = ('name','email', 'listing') #This allow you to be able to edit from the list
    search_fields = ('name', 'id','list_date')
    list_per_page = 15

admin.site.register(Product,  ProductAdmin)