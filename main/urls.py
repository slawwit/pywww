from django.urls import path
from main.views import about, hello_word

app_name = 'main'
urlpatterns = [
    path('', hello_word, name='hello_world'),
    path('about', about, name='about'),
]