from typing import List, Tuple, Type

from app.domain.authors.model import Author
from app.domain.authors.repository import AuthorRepository


class AuthorManager:
    model = Author

    @classmethod
    def get_authors(
        cls,
        cursor: str,
        page_size: int,
        name: str,
        using_repository: Type[AuthorRepository],
    ) -> Tuple[List[Author], str]:
        return using_repository.get_paginated_authors(
            cursor=cursor, limit=page_size, name=name
        )

    @classmethod
    def create_author(
        cls, author: Author, using_repository: AuthorRepository
    ) -> Author:
        return using_repository.create_author(author)

    @classmethod
    def delete_author(cls, name: str, using_repository: AuthorRepository) -> None:
        return using_repository.delete_author(name)
