import httpx
from app.core.config import settings


BASE_URL = "http://backend:8000/api/v1"


async def create_or_get_user(user_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/users",
            json=user_data
        )
        return response.json()
