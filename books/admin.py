from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Book, Author


class BookResource(resources.ModelResource):
    class Meta:
        model = Book


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ["id", "title", "available"]
    search_fields = ["title", "description"]
    list_filter = ["available"]
    resource_class = BookResource


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Book)
