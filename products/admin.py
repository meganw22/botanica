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
        'ease_of_care',
        'light',
        'price',
        'image',
        'description'
        ]

    ordering = (
        'easy_name', 
    )

admin.site.register(Product, ProductAdmin)