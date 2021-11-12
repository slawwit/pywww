from django.core.management import BaseCommand
from books.utils import create_books


class Command(BaseCommand):
    help = "Create fake books"

    def add_arguments(self, parser):
        parser.add_argument(
            "-n",
            "--number",
            type=int,
            default=10,
            dest='number',
            help='Amount of books'
        )

    def handle(self, *args, **options):
        create_books(
            options.get('number', 10)
        )
