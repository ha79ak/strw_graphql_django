import typing
import strawberry

@strawberry.type
class Book:
    title: str
    author: str

@strawberry.type
class Author:
    name: str
    book: str

def get_books():
    return [
        Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
        ),
        Book(
            title="Ince Memed",
            author="Yasar Kemal",
        ),
        Book(
            title="Kara Kitap",
            author="Orhan Pamuk",
        ),
    ]

def get_authors():
    return [
        Author(
            name="F. Scott Fitzgerald",
            book="The Great Gatsby",
        ),
        Author(
            name="Yasar Kemal",
            book="Ince Memed",
        ),
        Author(
            name="Orhan Pamuk",
            book="Kara Kitap",
        ),
    ]


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)
    authors: typing.List[Author] = strawberry.field(resolver=get_authors)

schema = strawberry.Schema(query=Query)
