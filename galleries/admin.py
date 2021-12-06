from django.contrib import admin
from .models import Gallery, Photo


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):  # admin.site.register(Post, PostAdmin)
    list_display = ["id", "title", 'slug', "status"]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):  # admin.site.register(Post, PostAdmin)
    list_display = ["id", "title", 'status']
