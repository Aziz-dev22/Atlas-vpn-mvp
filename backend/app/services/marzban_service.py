import httpx

from app.core.config import settings


class MarzbanService:

    def __init__(self):
        self.base_url = settings.MARZBAN_URL
        self.username = settings.MARZBAN_USERNAME
        self.password = settings.MARZBAN_PASSWORD
        self.token = None

    async def login(self):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/api/admin/token",
                json={
                    "username": self.username,
                    "password": self.password
                }
            )

            data = response.json()
            self.token = data.get("access_token")
            return self.token

    async def create_user(self, username: str, expire_days: int):

        if not self.token:
            await self.login()

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/api/user",
                headers=headers,
                json={
                    "username": username,
                    "expire": expire_days
                }
            )

            return response.json()
