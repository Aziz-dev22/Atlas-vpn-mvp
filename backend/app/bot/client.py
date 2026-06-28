import httpx


BASE_URL = "http://backend:8000/api/v1"


async def login_user(telegram_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/login",
            params={"telegram_id": telegram_id}
        )
        return response.json()


async def get_plans():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/plans")
        return response.json()


async def buy_plan(plan_id: int, token: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/buy/{plan_id}",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )
        return response.json()
