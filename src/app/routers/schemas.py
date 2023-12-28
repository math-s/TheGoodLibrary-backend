import logging
from typing import Annotated, Dict, List
from pycountry import countries
from pydantic import BaseModel, PastDate, StringConstraints, validator

logger = logging.getLogger(__name__)


class AuthorPayload(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=100)] = None
    birth_date: PastDate = None
    country: Annotated[str, StringConstraints(min_length=2, max_length=3)] = None
    languages: List[
        Annotated[str, StringConstraints(min_length=1, max_length=30)]
    ] = None


class PaginatedAuthor(BaseModel):
    authors: List[Dict]
    next_page_cursor: str | None
