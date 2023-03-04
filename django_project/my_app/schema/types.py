from typing import List

from django.contrib.auth import get_user_model
from strawberry import auto

import strawberry_django

from my_app import models

# import strawberry


# filters

@strawberry_django.filters.filter(models.Author, lookups=True)
class AuthorFilter:
    id: auto
    name: auto
    books: 'BookFilter'


@strawberry_django.filters.filter(models.Book, lookups=True)
class BookFilter:
    id: auto
    title: auto
    authors: AuthorFilter


# orders

@strawberry_django.ordering.order(models.Author)
class AuthorOrder:
    name: auto
    color: 'BookOrder'


@strawberry_django.ordering.order(models.Book)
class BookOrder:
    name: auto
    fruit: AuthorOrder



# types

@strawberry_django.type(
    models.Author, filters=AuthorFilter, order=AuthorOrder, pagination=True
)
class AuthorType:
    id: auto
    name: auto
    books: List['BookType']


@strawberry_django.type(
    models.Book, filters=BookFilter, order=BookOrder, pagination=True, description="Kitap oku.."
)
class BookType:
    id: auto
    title: auto
    author: AuthorType

    @classmethod
    def get_queryset(cls, queryset, info):
        print("//// ", info.context.request.user)
        return queryset.all()
        # if not info.context.request.user:
        #     return queryset.all()
        # None
        
@strawberry_django.input(models.Author)
class AuthorInput:
    id: auto
    name: auto
    books: auto


@strawberry_django.type(get_user_model())
class User:
    id: auto
    username: auto
    password: auto
    email: auto
