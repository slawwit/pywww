from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def show_library(request):
    pass
#     pos = 'sdgeherjhsdfhdsf'
#     list = range(1, 30, 3)
#     return render(request, 'books/list_books.html', {'pos': pos, 'pos2': list})


def books_details(request, books_id):
    book = Book.objects.get(pk=books_id)
    context = {"book": book}
    return render(request, "books/details.html", context)


def books_list(request):
    books = Book.objects.all()
    context = {"books_list": books}
    return render(request, "books/list.html", context)
