from strawberry.printer import print_schema

from django.core.management.base import BaseCommand

from strawberry_django_project.schema import schema


class Command(BaseCommand):
    def handle(self, *args, **options):
        sdl = print_schema(schema=schema)
        with open('schema.graphql', "w", encoding="utf-8") as outfile:
            outfile.write(sdl)
        self.stdout.write(self.style.SUCCESS(sdl))
