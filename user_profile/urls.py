from django.urls import path
from . import views
from .views import profile, edit_profile, delete_account, confirm_delete_account

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('delete/', confirm_delete_account, name='confirm_delete_account'),
    path('delete/confirm/', delete_account, name='delete_account'),
]

