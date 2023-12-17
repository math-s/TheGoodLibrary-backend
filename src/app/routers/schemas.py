import logging
from typing import Annotated, Dict, List

from pydantic import BaseModel, PastDate, StringConstraints

logger = logging.getLogger(__name__)


class AuthorPayload(BaseModel):
    # id: str = Field(default_factory=lambda: uuid4().hex)
    name: Annotated[str, StringConstraints(min_length=1, max_length=100)] = None
    birth_date: PastDate = None
    country: Annotated[str, StringConstraints(min_length=3, max_length=3)] = None
    language: Annotated[str, StringConstraints(min_length=1, max_length=30)] = None


class PaginatedAuthor(BaseModel):
    authors: List[Dict]
    next_page_cursor: str | None
