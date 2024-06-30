from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('newsletter_signup/', views.newsletter_signup, name='newsletter_signup'),
]
