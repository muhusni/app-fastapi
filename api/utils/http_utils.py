import httpx
from typing import Any, Dict, Optional

class AsyncHTTPClient:
    def __init__(self):
        self.client = httpx.AsyncClient()

    async def get(self, url: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, Any]] = None) -> httpx.Response:
        response = await self.client.get(url, headers=headers, params=params, timeout=None)
        response.raise_for_status()
        return response

    async def post(self, url: str, headers: Optional[Dict[str, str]] = None, json: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None) -> httpx.Response:
        response = await self.client.post(url, headers=headers, json=json, data=data, timeout=None)
        response.raise_for_status()
        return response

    async def put(self, url: str, headers: Optional[Dict[str, str]] = None, json: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None) -> httpx.Response:
        response = await self.client.put(url, headers=headers, json=json, data=data, timeout=None)
        response.raise_for_status()
        return response

    async def delete(self, url: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, Any]] = None) -> httpx.Response:
        response = await self.client.delete(url, headers=headers, params=params, timeout=None)
        response.raise_for_status()
        return response

    async def close(self):
        await self.client.aclose()
