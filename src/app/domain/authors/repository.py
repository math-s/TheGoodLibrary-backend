from abc import ABC

from typing import List, Tuple
from app.domain.authors.model import Author


class AuthorRepository(ABC):
    """
    Extend me to write the concrete Author Repository.
    I'm the interface for Author Repository.
    """

    def get_paginated_authors(
        self, cursor: str, limit: int, name: str = None
    ) -> Tuple[List[Author], str]:
        raise NotImplementedError()

    def get_author_by_id(self, id: int) -> Author:
        raise NotImplementedError()

    def create_author(self, author: Author) -> None:
        raise NotImplementedError()

    def update_author(self, id: int, author: Author) -> Author:
        raise NotImplementedError()

    def delete_author(self, id: int) -> None:
        raise NotImplementedError()
