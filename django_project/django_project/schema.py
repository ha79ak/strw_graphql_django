from typing import List

import strawberry

import strawberry_django
import strawberry_django.auth as auth
from strawberry_django import mutations

from my_app.schema.types import AuthorType, BookType


@strawberry.type
class Query:
    author: AuthorType = strawberry.django.field()
    authors: List[AuthorType] = strawberry.django.field()

    book: BookType = strawberry.django.field()
    books: List[BookType] = strawberry.django.field()


# @strawberry.type
# class Mutation:
#     createAuthor: AuthorType = mutations.create()
# ===>>> burdan devam.. https://github.com/strawberry-graphql/strawberry-graphql-django/blob/main/examples/django/app/schema.py

schema = strawberry.Schema(query=Query)
