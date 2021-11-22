from django.db import models
from common.models import Timestamped


class Book(Timestamped):
    title = models.CharField(max_length=255)
    description = models.TextField()
    available = models.BooleanField(default=False)
    publication_year = models.IntegerField()
    author = models.CharField(max_length=100)
    tags = models.ManyToManyField("tags.Tag", related_name="books")

    def __str__(self):
        return f"{self.id}{self.title} available: {self.available}"
