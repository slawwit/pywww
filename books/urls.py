from django.urls import path
from books.views import show_library, books_list, books_details

urlpatterns = [
    path('1', books_details),
    path('', books_list),
]