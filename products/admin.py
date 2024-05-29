from django.contrib import admin
from .models import Product, PlantSize

class PlantSizeInline(admin.TabularInline):
    model = PlantSize
    extra = 1

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
        'ease_of_care',
        'pet_ok',
        'light',
        'price',
        'image',
        'description'
    ]

    ordering = (
        'easy_name', 
    )

    inlines = [PlantSizeInline]

admin.site.register(Product, ProductAdmin)
