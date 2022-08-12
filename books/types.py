import strawberry

from books.models import Book


@strawberry.django.type(model=Book)
class BookType:
    pass
