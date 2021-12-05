from django.urls import path
from main.views import about, home, contact, user_profile

# app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('user/<int:user_id>/profile', user_profile, name='userprofile')
]