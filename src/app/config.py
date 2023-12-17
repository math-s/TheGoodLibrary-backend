import logging
import os


logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)


LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

AWS_SECRET_ID = os.getenv("AWS_SECRET_ID", "000000000")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY", "000000000")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AWS_ENDPOINT_URL = os.getenv("AWS_ENDPOINT_URL", "http://localhost:4566")

API_KEY_HEADER_NAME = "X-API-Key"
