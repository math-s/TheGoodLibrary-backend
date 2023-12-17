from datetime import date
import logging
from typing import Dict, List, Tuple

from app.adapters.authors_dynamodb import DynamoDBAuthorRepository
from app.domain.authors import Author, get_authors, get_authors_by_name, create_author
from app.routers.schemas import AuthorPayload

logger = logging.getLogger(__name__)


def fetch_authors(cursor: str, page_size: int) -> Tuple[List[Author], str]:
    logger.info("Fetching authors")

    authors, next_page_cursor = get_authors(
        cursor=cursor, page_size=page_size, using_repository=DynamoDBAuthorRepository()
    )

    return authors, next_page_cursor


def filter_authors_by_name(name: str, page: int, page_size: int):
    logger.info("Filtering authors by name")

    authors = get_authors_by_name(
        name=name,
        page=page,
        page_size=page_size,
        using_repository=DynamoDBAuthorRepository(),
    )

    return authors


def get_author_by_id(id: int):
    logger.info("Getting author by id")

    author = get_author_by_id(id=id, using_repository=DynamoDBAuthorRepository())

    return author


def get_or_create_author(payload: AuthorPayload) -> Author:
    logger.info("Creating author")

    # TODO: check if author already exists

    author = Author(
        name=payload.name,
        birth_date=payload.birth_date,
        country=payload.country,
        language=payload.language,
    )

    create_author(author=author, using_repository=DynamoDBAuthorRepository())

    return author
