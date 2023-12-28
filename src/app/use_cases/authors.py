import logging
from typing import List, Tuple

from app.adapters.authors_dynamodb import DynamoDBAuthorRepository
from app.domain.authors.manager import AuthorManager
from app.domain.authors import Author
from app.routers.schemas import AuthorPayload

logger = logging.getLogger(__name__)


def fetch_authors(
    cursor: str, page_size: int, name: str = None
) -> Tuple[List[Author], str]:
    logger.info("Fetching authors")

    authors, next_page_cursor = AuthorManager.get_authors(
        cursor=cursor,
        page_size=page_size,
        name=name,
        using_repository=DynamoDBAuthorRepository(),
    )

    return authors, next_page_cursor


def filter_authors_by_name(
    cursor: str, page_size: int, name: str
) -> Tuple[List[Author], str]:
    logger.info("Filtering authors by name")

    authors, next_page_cursor = AuthorManager.get_authors(
        cursor=cursor, page_size=page_size, using_repository=DynamoDBAuthorRepository()
    )

    return authors, next_page_cursor


def get_or_create_author(payload: AuthorPayload) -> Author:
    logger.info("Creating author")

    # TODO: check if author already exists

    author = Author(
        name=payload.name,
        birth_date=payload.birth_date,
        country=payload.country,
        languages=payload.languages,
    )

    return AuthorManager.create_author(
        author=author, using_repository=DynamoDBAuthorRepository()
    )
