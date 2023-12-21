import logging

from prettyconf import config


logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)


LOG_LEVEL = config("LOG_LEVEL")

AWS_SECRET_ID = config("AWS_SECRET_ID")
AWS_ACCESS_KEY = config("AWS_ACCESS_KEY")
AWS_REGION = config("AWS_REGION")
AWS_ENDPOINT_URL = config("AWS_ENDPOINT_URL")

API_KEY_HEADER_NAME = "X-API-Key"
