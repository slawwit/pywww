from django.shortcuts import render, get_object_or_404
from .forms import BookForm
from django.http import HttpResponseRedirect
from .models import Book
from django.urls import reverse


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


def edit_book(request, books_id):
    book = get_object_or_404(Book, pk=books_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
    else:
        form = BookForm(instance=book)
    return render(request, 'books/add.html', {'form': form})


def add_book(request):
    if request.method == "POST" and request.user.is_authenticated:
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse("books:add"))
    else:
        form = BookForm()
    return render(request, 'books/add.html', {'form': form})

