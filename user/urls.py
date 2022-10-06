from django.urls import path
from .views import add_user, about_user, all_users

urlpatterns = [
    path('', add_user, name='add_user'),
    path('about_user/<slug:user_slug>', about_user, name='about_user'),
    path('all_users/', all_users, name='all_users'),
]
