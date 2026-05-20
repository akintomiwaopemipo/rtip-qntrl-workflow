from typing import Any

import httpx

from src.core.config import settings
from src.integrations.qntrl.auth import auth_manager


BASE_URL = (
    f"https://coreapi.qntrl.com/"
    f"blueprint/api"
)

API_URL = (
    f"{BASE_URL}/{settings.qntrl_org_id}"
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
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        data: dict[str, Any] | None = None,
        files: dict[str, Any] | None = None,
        timeout: httpx.Timeout | None = None,
    ) -> dict[str, Any]:

        token = await auth_manager.get_access_token()

        headers = headers or {}

        headers["Authorization"] = (
            f"Zoho-oauthtoken {token}"
        )
        
        

        endpoint = endpoint if endpoint.startswith("/") else f"/{endpoint}"

        response = await self.client.request(
            method=method,
            url=f"{API_URL}{endpoint}",
            headers=headers,
            params=params,
            json=json,
            data=data,
            files=files,
            timeout=timeout
        )

        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            print(f"Request failed: {exc.response.status_code} - {exc.response.text}")
            raise exc

        return response.json()

    
    
    async def base_request(
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

        endpoint = endpoint if endpoint.startswith("/") else f"/{endpoint}"

        response = await self.client.request(
            method=method,
            url=f"{BASE_URL}{endpoint}",
            headers=headers,
            **kwargs
        )

        response.raise_for_status()

        return response.json()


qntrl_client = QntrlClient()
