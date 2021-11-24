# from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from common.models import Timestamped


# Create your models here.


class Post(Timestamped):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True)
    # modified = models.DateTimeField(auto_now=True)
    sponsored = models.BooleanField(default=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    tags = models.ManyToManyField('tags.Tag', related_name="posts")
    category = models.ManyToManyField('posts.Category')
    example_file = models.FileField(upload_to='posts/examples/', blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True, editable=False)
    image = models.ImageField(upload_to="posts/images/%Y/%m/%d/", null=True, width_field="image_width")

    def __str__(self):
        return f"{self.id}  {self.title}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.id}  {self.name}"
