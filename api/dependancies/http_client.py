from typing import Annotated
from fastapi import Depends
from api.utils import AsyncHTTPClient

# Dependency function to provide an instance of AsyncHTTPClient
async def get_http_client():
    client = AsyncHTTPClient()
    try:
        yield client
    finally:
        await client.close()

# Annotated type hint for dependency injection
HttpClient = Annotated[AsyncHTTPClient, Depends(get_http_client)]
