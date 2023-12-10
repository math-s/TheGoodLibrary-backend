from pydantic import BaseModel


class Author(BaseModel):
    id: int
    name: str
    email: str | None = None


class Book(BaseModel):
    id: int
    title: str
    subtitle: str
    description: str
    isbn: str
    author: Author


class Edition(BaseModel):
    id: int
    edition: int
    year: int
    publisher: str
    book: Book
    pages: int
