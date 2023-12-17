from typing import List, Tuple
from app.domain.authors import Author, AuthorRepository
from .dynamodb import BaseDynamoRepository, handle_dynamodb_client_error
import base64


class DynamoDBAuthorRepository(AuthorRepository, BaseDynamoRepository):
    table_name = "Authors"

    @handle_dynamodb_client_error()
    def get_paginated_authors(
        self, cursor: str, limit: int
    ) -> Tuple[List[Author], str]:
        if cursor:
            data = self.table.scan(
                ExclusiveStartKey={"name": base64.b64decode(cursor).decode()},
                Limit=limit,
            )
        else:
            data = self.table.scan(Limit=limit)

        last_key = data.get("LastEvaluatedKey", None)

        new_cursor = (
            base64.b64encode(last_key["name"].encode("utf-8")) if last_key else None
        )
        return [Author(**info) for info in data["Items"]], new_cursor

    @handle_dynamodb_client_error()
    def get_author_by_id(self, id: int) -> Author:
        data = self.table.get_item(
            Key={
                "name": id,
            }
        )

        return Author(**data.get("Item", {}))

    @handle_dynamodb_client_error()
    def create_author(self, author: Author) -> None:
        self.table.put_item(Item=author.as_dict)

    def update_author(self, id: int, author: Author) -> Author:
        raise NotImplementedError()

    def delete_author(self, id: int) -> None:
        raise NotImplementedError()

    def get_author_by_name(self, name: str, cursor: int, limit: int) -> List[Author]:
        raise NotImplementedError()
