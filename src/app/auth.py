from fastapi import FastAPI, Depends, Header
from fastapi.security import APIKeyHeader

from .config import API_KEY_HEADER_NAME


api_key_header = APIKeyHeader(name=API_KEY_HEADER_NAME, auto_error=False)


async def authenticate(api_key: str = Header(API_KEY_HEADER_NAME)) -> bool:
    return True
