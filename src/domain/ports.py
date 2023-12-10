from abc import ABC
from typing import List
from domain.models import Author


class AuthorRepository(ABC):
    """
    Extend me to write the concrete Author Repository.
    """

    def get_paginated_authors(self, offset: int, limit: int) -> List[Author]:
        raise NotImplementedError()

    def get_author_by_id(self, id: int) -> Author:
        raise NotImplementedError()

    def create_author(self, author: Author) -> Author:
        raise NotImplementedError()

    def update_author(self, id: int, author: Author) -> Author:
        raise NotImplementedError()

    def delete_author(self, id: int) -> None:
        raise NotImplementedError()

    def get_author_by_name(self, name: str, offset: int, limit: int) -> List[Author]:
        raise NotImplementedError()
