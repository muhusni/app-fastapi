import httpx
from typing import Any, Dict, Optional, Tuple

class AsyncHTTPClient:
    def __init__(self):
        self.client = httpx.AsyncClient()

    async def get(self, url: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, Any]] = None, auth: Tuple[str, str] = None) -> httpx.Response:
        response = await self.client.get(url, auth=auth, headers=headers, params=params, timeout=None)
        response.raise_for_status()
        return response

    async def post(self, url: str, headers: Optional[Dict[str, str]] = None, json: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None, auth: Tuple[str, str] = None) -> httpx.Response:
        response = await self.client.post(url, auth=auth, headers=headers, json=json, data=data, timeout=None)
        response.raise_for_status()
        return response

    async def put(self, url: str, headers: Optional[Dict[str, str]] = None, json: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None, auth: Tuple[str, str] = None) -> httpx.Response:
        response = await self.client.put(url, auth=auth, headers=headers, json=json, data=data, timeout=None)
        response.raise_for_status()
        return response

    async def delete(self, url: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, Any]] = None, auth: Tuple[str, str] = None) -> httpx.Response:
        response = await self.client.delete(url, auth=auth, headers=headers, params=params, timeout=None)
        response.raise_for_status()
        return response
    
    async def download_file(self, url: str, headers: Optional[Dict[str, str]] = None, auth: Tuple[str, str] = None):
        async with self.client.stream("GET", url, auth=auth, headers=headers) as response:
            response.raise_for_status()
            return response

    async def close(self):
        await self.client.aclose()
