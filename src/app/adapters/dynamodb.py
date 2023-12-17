import boto3
import logging
from abc import ABC
from app.config import AWS_REGION, AWS_ENDPOINT_URL


logger = logging.getLogger("api")


class BaseDynamoRepository(ABC):
    table_name: str

    def __init__(self):
        self.dynamodb = boto3.resource(
            "dynamodb", region_name=AWS_REGION, endpoint_url=AWS_ENDPOINT_URL
        )
        self.table = self.dynamodb.Table(self.table_name)


def handle_dynamodb_client_error(*args, **kwargs):
    # decorator to handle dynamodb client errors
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                logger.error(
                    f"Couldn't complete operation {func.__name__}",
                    extra={
                        "props": {
                            "args": [*args],
                            "kwargs": {**kwargs},
                        }
                    },
                )
                raise err

        return wrapper

    return decorator
