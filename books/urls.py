from django.urls import path
from books.views import show_library, books_list, books_details, add_book, edit_book

app_name = "books"
urlpatterns = [
    path('add', add_book, name="add"),
    path('<int:books_id>', books_details, name="details"),
    path('', books_list, name="list"),
    path('<int:books_id>/edit', edit_book, name='edit')
]
