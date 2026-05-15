import time
import httpx

from src.core.config import settings
from src.core.logging import logger


ZOHO_TOKEN_URL = "https://accounts.zoho.com/oauth/v2/token"


class QntrlAuthManager:

    def __init__(self):
        self.access_token = None
        self.expires_at = 0

    async def get_access_token(self) -> str:

        if (
            self.access_token and
            time.time() < self.expires_at
        ):
            return self.access_token

        logger.info("Refreshing Qntrl access token")

        params = {
            "refresh_token": settings.qntrl_refresh_token,
            "client_id": settings.qntrl_client_id,
            "client_secret": settings.qntrl_client_secret,
            "grant_type": "refresh_token",
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                ZOHO_TOKEN_URL,
                params=params
            )

            response.raise_for_status()

            data = response.json()

            self.access_token = data["access_token"]

            expires_in = data.get("expires_in", 3600)

            self.expires_at = time.time() + expires_in - 60

            return self.access_token


auth_manager = QntrlAuthManager()
