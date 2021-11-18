from django.contrib import admin
from .models import Post, Category
from import_export import resources
from import_export.admin import ExportMixin


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


@admin.register(Post)
class PostAdmin(ExportMixin, admin.ModelAdmin):  # admin.site.register(Post, PostAdmin)
    list_display = ["id", "title", "created", "modified", "published", "sponsored"]
    search_fields = ["title", "content"]
    list_filter = ["published", "sponsored"]
    resource_class = PostResource


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  # admin.site.register(Post, PostAdmin)
    list_display = ["id", "name"]
