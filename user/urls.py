from django.urls import path
from .views import add_user, about_user

urlpatterns = [
    path('add/', add_user, name='add_user'),
    path('about_user/<slug:user_slug>', about_user, name='about_user'),
]
