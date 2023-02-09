import typing
import strawberry




@strawberry.type
class Book:
    title: str
    author: str

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

@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)


schema = strawberry.Schema(query=Query)

