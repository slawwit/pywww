from django.shortcuts import render, redirect
from galleries.models import Gallery
from .forms import GalleryForm, PhotoForm
from django.urls import reverse


def gallery_list(request):
    galleries = Gallery.objects.filter(status='published')
    return render(request, 'galleries/list.html', {'galleries': galleries})


def gallery_details(request, gallery_id):
    gallery = Gallery.objects.get(pk=gallery_id)
    context = {'gallery': gallery}
    return render(request, 'galleries/details.html', context)


def add_gallery(request):
    form = GalleryForm()
    if request.method == "POST" and request.user.is_authenticated:
        form = GalleryForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.save()
            return redirect(reverse('galleries:add_gallery'))
    return render(request, 'galleries/add_gallery.html', {'form': form})


def add_photo(request):
    form = PhotoForm()
    if request.method == "POST" and request.user.is_authenticated:
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.save()
            return redirect(reverse('galleries:add_photo'))
    return render(request, 'galleries/add_photo.html', {'form': form})
