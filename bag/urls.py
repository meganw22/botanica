from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_bag, name='shopping_bag'),
    path('add_to_bag/<int:product_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust_bag/<int:product_id>/', views.adjust_bag, name='adjust_bag'),
    path(
        'remove_from_bag/<int:product_id>/<str:height>/',
        views.remove_from_bag,
        name='remove_from_bag'
        ),
]
