from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'easy_name',
        'scientific_name',
        'price',
        'image',
    )

    fields = [
        'easy_name',
        'scientific_name',
        'height',
        'care_level',
        'light_level',
        'price',
        'image',
        'description'
        ]

    ordering = (
        'easy_name', 
    )

admin.site.register(Product, ProductAdmin)