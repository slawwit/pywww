from django.urls import path
from books.views import show_library, books_list, books_details, add_book, edit_book, handle_book_borrows

app_name = "books"
urlpatterns = [
    path('', books_list, name="list"),
    path('add', add_book, name="add"),
    path('<int:book_id>', books_details, name="details"),
    path('<int:book_id>/borrows', handle_book_borrows, name="borrows"),
    path('borrows', handle_book_borrows, name="borrows_list"),
    path('<int:book_id>/edit', edit_book, name='edit')
]
