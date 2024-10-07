from fastapi import Security
from fastapi.security import APIKeyHeader

token_header = APIKeyHeader(name="Authorization", auto_error=False)


async def validate_token(token: str = Security(token_header)):
    """To be implemented"""
    ...
