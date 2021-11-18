#from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta


# Create your models here.
class CheckAgeMixin:
    def is_older_than_n_days(self, n=1):
        delta = timedelta(days=n)
        return now() - self.created > delta


class Timestamped(models.Model, CheckAgeMixin):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(models.Model, CheckAgeMixin):
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