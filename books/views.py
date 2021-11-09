from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def show_library(request):
    pos = 'sdgeherjhsdfhdsf'
    list = range(1,30,3)
    return render(request, 'books/list_books.html', {'pos': pos,'pos2':list})
