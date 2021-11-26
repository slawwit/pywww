from django.urls import path
from main.views import about, hello_word, contact, user_profile

# app_name = 'main'

urlpatterns = [
    path('', hello_word, name='hello_world'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('user/<int:user_id>/profile', user_profile, name='userprofile')
]