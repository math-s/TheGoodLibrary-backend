from dataclasses import dataclass


@dataclass
class Book:
    id: int
    title: str
    subtitle: str
    description: str
    author: "Author"


@dataclass
class Edition:
    id: int
    edition: int
    year: int
    publisher: str
    book: Book
    pages: int
    isbn: str
