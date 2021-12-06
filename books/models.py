from django.db import models
from common.models import Timestamped
from sorl.thumbnail import ImageField


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
    tags = models.ManyToManyField("tags.Tag", related_name="books", blank=True)
    authors = models.ManyToManyField(Author, related_name="books")
    cover = ImageField(upload_to='books/covers/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return f"{self.id}{self.title} available: {self.available}"


class Borrow(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="borrows")
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="borrows")
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
