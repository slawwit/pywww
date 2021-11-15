from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "available"]
    search_fields = ["title", "author", "description"]
    list_filter = ["available"]

# admin.site.register(Book)
