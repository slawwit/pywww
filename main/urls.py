from django.urls import path
from main.views import about, hello_word

urlpatterns = [
    path('', hello_word),
    path('about', about)
]