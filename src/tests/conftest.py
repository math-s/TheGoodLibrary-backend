from typing import Optional

import boto3

from app.config import AWS_REGION
from .data import AUTHORS


def get_dynamodb_table(table_name: str):
    dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
    return dynamodb.Table(table_name)


def setup_db() -> None:
    dynamodb = boto3.client("dynamodb", region_name=AWS_REGION)

    dynamodb.create_table(
        TableName='Authors',
        BillingMode='PAY_PER_REQUEST',
        KeySchema=[
            {
                'AttributeName': 'name',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'country',
                'AttributeType': 'S'
            }
        ],
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'GSI1',
                'KeySchema': [
                    {
                        'AttributeName': 'name',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'country',
                        'KeyType': 'RANGE'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                }
            }
        ],
    )


def add_item(table_name: str, item) -> None:
    table = get_dynamodb_table(table_name)
    table.put_item(Item=item)


def get_item(table_name: str, keys) -> Optional[dict]:
    table = get_dynamodb_table(table_name)
    response = table.get_item(Key=keys)

    if "Item" not in response:
        return None

    return response["Item"]


def populate_authors():

    for author in AUTHORS:
        add_item("Authors", author)
