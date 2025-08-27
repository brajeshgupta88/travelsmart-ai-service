import httpx
from tenacity import AsyncRetrying, stop_after_attempt, wait_exponential

async def get_json(url: str, headers: dict = None, params: dict = None, timeout: int = 10):
    async with httpx.AsyncClient(timeout=timeout) as client:
        async for attempt in AsyncRetrying(stop=stop_after_attempt(3), wait=wait_exponential()):
            with attempt:
                resp = await client.get(url, headers=headers, params=params)
                resp.raise_for_status()
                return resp.json()
