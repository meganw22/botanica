from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'easy_name',
        'scientific_name',
        'height',
        'price',
    )

    ordering = (
        'easy_name', 
    )

admin.site.register(Product, ProductAdmin)