import string
from random import random
from django.utils.text import slugify
from django.db import models
from common.models import Timestamped, SlugMixin


STATUS_CHOICES = [
        ('hide', 'hide'),
        ('published', 'published'),
        ('new', 'new'),
    ]


class Gallery(Timestamped, SlugMixin):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="new")

    def __str__(self):
        return self.title


def uploud_to(instance, filename):
    return f"galleries/{instance.gallery.slug}/{filename}"


class Photo(Timestamped):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    short_description = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to="")
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name="photos")
    source = models.CharField(max_length=512, null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="new")

    def __str__(self):
        return self.slug
