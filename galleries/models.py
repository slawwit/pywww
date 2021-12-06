import string
from random import random
from django.db import models
from common.models import Timestamped
from django.utils.text import slugify

STATUS_CHOICES = [
        ('hide', 'hide'),
        ('published', 'published'),
        ('new', 'new'),
    ]


def get_random_text(n):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(n))


class Gallery(Timestamped):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="new")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self._state.adding and not self.slug:
            slug = slugify(self.title)
            slugs = self.__class__.objects.values_list('slug', flat=True)
            if slugs:
                while True:
                    if slug in slugs:
                        slug += get_random_text(5)
                    else:
                        break
            self.slug = slug
        return super().save(*args, **kwargs)


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
