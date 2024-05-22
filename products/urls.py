from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('filter/', views.filter_products, name='filter_products'),
    path('add_to_bag/<int:product_id>/', views.add_to_bag, name='add_to_bag'),
    path('remove_from_bag/<int:product_id>/<str:height>/', views.remove_from_bag, name='remove_from_bag'),
    path('bag/', views.shopping_bag, name='shopping_bag'),
]