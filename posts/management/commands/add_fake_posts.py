from django.core.management import BaseCommand
from posts.utils import create_posts


class Command(BaseCommand):
    help = "Create fake posts"

    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            '--number',
            type=int,
            default=10,
            dest="number",
            help="Amount of posts"
        )

    def handle(self, *args, **options):
        create_posts(
            options.get("number", 10)
        )
        self.stdout.write('Posts has benn created!')