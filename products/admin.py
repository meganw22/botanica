from django.contrib import admin
from .models import Product, PlantSize, PlantPrice

class PlantSizeInline(admin.TabularInline):
    model = PlantSize
    extra = 0

class PlantPriceInline(admin.TabularInline):
    model = PlantPrice
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'easy_name',
        'scientific_name',
        'image',
        'pet_ok',
    )

    fields = [
        'easy_name',
        'scientific_name',
        'ease_of_care',
        'pet_ok',
        'light',
        'image',
        'description'
    ]

    ordering = (
        'easy_name', 
    )

    inlines = [PlantSizeInline, PlantPriceInline]

admin.site.register(Product, ProductAdmin)
