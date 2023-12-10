from fastapi import APIRouter


router = APIRouter(
    prefix="/authors",
    tags=["authors"]
)


@router.get("/")
def fetch_authors():
    return {
        "authors": [],
        "page": 0
    }
