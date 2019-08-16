from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','list_date','price')
    list_display_links = ('id','name')
    list_filter = ('name',)
    list_editable = ('price',) #This allow you to be able to edit from the list
    search_fields = ('name', 'id','list_date')
    list_per_page = 15

admin.site.register(Product,  ProductAdmin)


# class TagAdmin(admin.ModelAdmin):
#     list_display = ('id','title')
#     list_filter  = ('title',)
#     search_fields = ('title', 'id', 'time_stamp')
#     list_editable = ('title',)

# admin.site.register(Tag, TagAdmin)