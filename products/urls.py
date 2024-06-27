from django.urls import path
from . import views
from .views import filter_category_products, all_products, product_detail


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('filter/', views.filter_products, name='filter_products'),
    path('filter/bright-light/', filter_category_products, {'light': 'bright'}, name='filter_bright_light'),
    path('filter/low-light/', filter_category_products, {'light': 'low'}, name='filter_low_light'),
    path('filter/easy-maintenance/', filter_category_products, {'ease_of_care': 'easy'}, name='filter_easy_maintenance'),
    path('filter/expert/', filter_category_products, {'ease_of_care': 'difficult'}, name='filter_expert'),
    path('filter/lowest-to-highest-price/', filter_category_products, {'order': 'price_asc'}, name='filter_price_asc'),
    path('filter/highest-to-lowest-price/', filter_category_products, {'order': 'price_desc'}, name='filter_price_desc'),
]