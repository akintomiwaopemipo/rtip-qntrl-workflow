from typing import Any

import httpx

from src.core.config import settings
from src.integrations.qntrl.auth import auth_manager


BASE_URL = (
    f"https://coreapi.qntrl.com/"
    f"blueprint/api/{settings.qntrl_org}"
)


class QntrlClient:

    def __init__(self):
        self.client = httpx.AsyncClient(
            timeout=30.0
        )

    async def request(
        self,
        method: str,
        endpoint: str,
        **kwargs: Any
    ) -> dict[str, Any]:

        token = await auth_manager.get_access_token()

        headers = kwargs.pop("headers", {})

        headers["Authorization"] = (
            f"Zoho-oauthtoken {token}"
        )

        response = await self.client.request(
            method=method,
            url=f"{BASE_URL}{endpoint}",
            headers=headers,
            **kwargs
        )

        response.raise_for_status()

        return response.json()


qntrl_client = QntrlClient()
