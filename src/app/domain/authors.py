from abc import ABC
from datetime import date
from typing import Dict
from dataclasses import dataclass
from typing import List, Type, Tuple
from datetime import datetime


@dataclass
class Author:
    name: str
    birth_date: date
    country: str
    language: str
    # TODO: add lib pycountry to validate country and language

    def __post_init__(self) -> None:
        self.birth_date = (
            datetime.fromisoformat(self.birth_date).date() if self.birth_date else None
        )

    @property
    def first_name(self) -> str:
        return self.name.split(" ")[0]

    def __eq__(self, __value: "Author") -> bool:
        if self.__class__ != __value.__class__:
            return False
        return self.name == __value.name and self.birth_date == __value.birth_date

    @property
    def as_dict(self) -> Dict:
        return {
            "name": self.name,
            "birth_date": self.birth_date.isoformat() if self.birth_date else None,
            "country": self.country,
            "language": self.language,
        }


class AuthorRepository(ABC):
    """
    Extend me to write the concrete Author Repository.
    I'm the interface for Author Repository.
    """

    def get_paginated_authors(
        self, cursor: int, limit: int
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

    def get_author_by_name(self, name: str, cursor: int, limit: int) -> List[Author]:
        raise NotImplementedError()


def get_authors(
    cursor: str, page_size: int, using_repository: Type[AuthorRepository]
) -> Tuple[List[Author], str]:
    return using_repository.get_paginated_authors(cursor=cursor, limit=page_size)


def get_authors_by_name(name: str, using_repository: AuthorRepository) -> List[Author]:
    return using_repository.get_author_by_name(name)


def create_author(author: Author, using_repository: AuthorRepository) -> Author:
    return using_repository.create_author(author)


def update_author(
    id: int, author: Author, using_repository: AuthorRepository
) -> Author:
    return using_repository.update_author(id, author)


def delete_author(id: int, using_repository: AuthorRepository) -> None:
    return using_repository.delete_author(id)
