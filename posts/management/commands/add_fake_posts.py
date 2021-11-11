from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "add posts"

    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--number',
            type=int, default=10,dest="number",
            help="Amount of posts"
        )

    def handle(self, *args, **options):
        n = options.get("number", 10)

