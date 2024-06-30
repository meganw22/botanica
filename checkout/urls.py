from django.urls import path
from . import views
from .views import stripe_webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success/<str:order_id>/', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('webhook/', stripe_webhook, name='stripe-webhook'),
]
