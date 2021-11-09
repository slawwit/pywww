from django.shortcuts import render
from django.http import HttpResponse


def hello_word(request):
    return HttpResponse('Moja aplikacja')


def about(request):
    return render(request, "main/about.html", {})
