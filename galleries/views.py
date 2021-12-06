from django.shortcuts import render
from galleries.models import Gallery


def gallery_list(request):
    galleries = Gallery.objects.filter(status='published')
    return render(request, 'galleries/list.html', {'galleries': galleries})
