from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    sponsored = models.BooleanField(default=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    tags = models.ManyToManyField('tags.Tag', related_name="posts")
    category = models.ManyToManyField('posts.Category')

    def __str__(self):
        return f"{self.id}  {self.title}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.id}  {self.name}"