from django.urls import path
from books.views import show_library, books_list, books_details

app_name = "books"
urlpatterns = [
    path('<int:books_id>', books_details, name="details"),
    path('', books_list, name="list"),
]