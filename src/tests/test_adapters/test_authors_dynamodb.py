import base64
from typing import List, Tuple

import pytest

from app.domain.authors import Author, AuthorRepository
from app.adapters import DynamoDBAuthorRepository
from tests.conftest import setup_db, populate_authors
from moto import mock_dynamodb


@mock_dynamodb
def test_get_paginated_authors():

    setup_db()
    populate_authors()

    authors, cursor = DynamoDBAuthorRepository().get_paginated_authors(
        cursor=None, limit=2
    )

    assert len(authors) == 2


def test_create_author():
    pass
