from django.contrib import admin
from .models import Cart
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('id','total','create_date')
    list_display_links = ('id',)
    list_filter = ('create_date','update_date')
    # list_editable = ('name','email', 'listing') #This allow you to be able to edit from the list
    search_fields = ('create_date', 'id','update_date')
    list_per_page = 15

admin.site.register(Cart,  CartAdmin)

