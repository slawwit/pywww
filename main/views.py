from django.shortcuts import render
from django.http import HttpResponse


def hello_word(request):
    return render(request, 'main/hello_world.html')


def about(request):
    return render(request, "main/about.html", {})
