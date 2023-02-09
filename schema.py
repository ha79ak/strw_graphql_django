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
            title="Grinin 49 Tonu",
            author="Acaip Birikayip",
        ),
    ]

@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)


schema = strawberry.Schema(query=Query)

