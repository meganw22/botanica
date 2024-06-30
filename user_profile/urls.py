from django.urls import path
from . import views
from .views import delete_account, confirm_delete_account

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('manage_addresses/', views.manage_addresses, name='manage_addresses'),
    path('edit_address/<int:address_id>/', views.edit_address, name='edit_address'),
    path('delete_address/<int:address_id>/', views.delete_address, name='delete_address'),
    path('delete/', confirm_delete_account, name='confirm_delete_account'),
    path('delete/confirm/', delete_account, name='delete_account'),
]
