from django.shortcuts import render, get_object_or_404
from .forms import BookForm, BookBorrowForm
from django.http import HttpResponseRedirect
from .models import Book, Borrow
from django.urls import reverse
from django.utils import timezone


def show_library(request):
    pass


#     pos = 'sdgeherjhsdfhdsf'
#     list = range(1, 30, 3)
#     return render(request, 'books/list_books.html', {'pos': pos, 'pos2': list})


def books_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookBorrowForm()
    form.helper.form_action = reverse("books:borrows", args=[book.id])
    context = {"book": book, "form": form}
    return render(request, "books/details.html", context)


def books_list(request):
    books = Book.objects.all()
    context = {"books_list": books}
    return render(request, "books/list.html", context)


def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
    else:
        form = BookForm(instance=book)
    return render(request, 'books/add.html', {'form': form})


def add_book(request):
    form = BookForm()
    if request.method == "POST" and request.user.is_authenticated:
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse("books:add"))

    return render(request, 'books/add.html', {'form': form})


def handle_book_borrows(request, book_id=None):
    user = request.user
    if request.method == 'POST':
        if user.is_authenticated:
            if request.POST.get('borrow'):
                book = Book.objects.get(pk=book_id)
                Borrow.objects.create(
                    user=user,
                    book=book
                )
                book.available = False
                book.save()
                return HttpResponseRedirect(reverse("books:details", args=[book_id]))
            else:
                keys = [key for key in request.POST.keys() if key.startswith("book_")]
                print(keys)
                key = int(keys[0].split("_")[1])
                book = Book.objects.get(pk=key)
                borrow = Borrow.objects.filter(user=user, book=book).last()
                if not borrow.return_date:
                    borrow.return_date = timezone.now()
                    borrow.save()
                    book.available = True
                    book.save()
                return HttpResponseRedirect(reverse("books:borrows_list"))
    else:
        borrows = Borrow.objects.filter(user=user)
        return render(request, "books/borrows_list.html", {"borrows": borrows})
