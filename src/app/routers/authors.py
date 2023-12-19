from fastapi import APIRouter, Security

from app.auth import authenticate
from app.services.authors import fetch_authors as fetch_authors_service
from app.services.authors import get_or_create_author as get_or_create_author
from app.routers.schemas import PaginatedAuthor, AuthorPayload


router = APIRouter(prefix="/authors", tags=["authors"])


@router.get("/", status_code=200, response_model=PaginatedAuthor)
def fetch_authors(cursor: str = None, page_size: int = 10, name: str = None):
    # TODO: breaking for invalid cursor
    authors, next_page_cursor = fetch_authors_service(
        cursor=cursor, page_size=page_size, name=name
    )

    return {
        "authors": [author.as_dict for author in authors],
        "next_page_cursor": next_page_cursor,
    }


@router.post("/")
def create_author(payload: AuthorPayload, api_key: str = Security(authenticate)):
    get_or_create_author(payload)

    return {"message": "Author created."}
