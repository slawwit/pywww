from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):  # admin.site.register(Post, PostAdmin)
    list_display = ["id", "title", "created", "modified", "published", "sponsored"]
    search_fields = ["title", "content"]
    list_filter = ["published", "sponsored"]
