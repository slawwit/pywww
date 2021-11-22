from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Book


class BookResource(resources.ModelResource):
    class Meta:
        model = Book


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ["id", "title", "author", "available"]
    search_fields = ["title", "author", "description"]
    list_filter = ["available"]
    resource_class = BookResource

# admin.site.register(Book)
