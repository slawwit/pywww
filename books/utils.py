from faker import Faker
from .models import Book
from random import randint


def create_books(n=2):
    fake = Faker("pl_PL")
    for _ in range(n):
        book = Book(
            title=fake.text(randint(7, 30)),
            description=fake.text(randint(40, 300)),
            available=fake.boolean(),
            publication_year=int(fake.year()),
            author=fake.name()
        )
        book.save()
