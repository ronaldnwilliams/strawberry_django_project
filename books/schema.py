from typing import List

import strawberry
import strawberry_django

from books.types import BookType


@strawberry.type
class Query:
    all_books: List[BookType] = strawberry_django.field()
