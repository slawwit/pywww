from django.db import models
from common.models import Timestamped


class Author(Timestamped):
    name = models.CharField(max_length=200)
    birth_year = models.IntegerField()
    death_year = models.IntegerField(blank=True, null=True)
    biogram = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.birth_year} - {self.death_year})"


class Book(Timestamped):
    title = models.CharField(max_length=255)
    description = models.TextField()
    available = models.BooleanField(default=False)
    publication_year = models.IntegerField()
    tags = models.ManyToManyField("tags.Tag", related_name="books")
    authors = models.ManyToManyField(Author, related_name="books")
    cover_width = models.IntegerField(blank=True, null=True, editable=False)
    cover = models.ImageField(upload_to='books/covers/%Y/%m/%d', null=True, width_field='cover_width')

    def __str__(self):
        return f"{self.id}{self.title} available: {self.available}"
