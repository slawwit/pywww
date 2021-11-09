from django.urls import path
from books.views import show_library


urlpatterns = [
    path('', show_library)
]