import base64
import logging
from datetime import datetime
from typing import List, Tuple

from boto3.dynamodb.conditions import Attr

from app.domain.authors import Author, AuthorRepository

from .dynamodb import BaseDynamoRepository, handle_dynamodb_client_error

logger = logging.getLogger(__name__)


class DynamoDBAuthorRepository(AuthorRepository, BaseDynamoRepository):
    table_name = "Authors"

    @handle_dynamodb_client_error()
    def get_paginated_authors(
        self, cursor: str, limit: int, name: str = None
    ) -> Tuple[List[Author], str]:
        # TODO: add constraint to name length for performance ?? O(m*n)
        author_name = name
        kwargs_filter = {}

        if cursor:
            kwargs_filter["ExclusiveStartKey"] = {
                "name": base64.b64decode(cursor).decode()
            }

        if author_name:
            kwargs_filter["FilterExpression"] = "contains(#n, :author_name)"
            kwargs_filter["ExpressionAttributeNames"] = {"#n": "name"}
            kwargs_filter["ExpressionAttributeValues"] = {":author_name": author_name}

        kwargs_filter["Limit"] = limit

        if "KeyConditionExpression" in kwargs_filter:
            data = self.table.query(**kwargs_filter)
        else:
            data = self.table.scan(**kwargs_filter)

        last_key = data.get("LastEvaluatedKey", None)

        new_cursor = (
            base64.b64encode(last_key["name"].encode("utf-8")) if last_key else None
        )
        return [Author(**info) for info in data["Items"]], new_cursor

    @handle_dynamodb_client_error()
    def create_author(self, author: Author) -> Author:
        try:
            self.table.put_item(
                Item=author.as_dict,
                ConditionExpression=Attr("name").ne(author.name),
            )
        except Exception as err:
            logger.warning(f"Error: {err}")
            return None
        return author

    def update_author(self, id: int, author: Author) -> Author:
        raise NotImplementedError()

    def delete_author(self, id: int) -> None:
        raise NotImplementedError()
