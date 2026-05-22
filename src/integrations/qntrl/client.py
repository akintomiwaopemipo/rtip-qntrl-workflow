from typing import Any
import json as json_module

from fastapi import HTTPException
import httpx

from src.core.config import settings
from src.domain.api.http_client import HttpMethod
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

    async def _request(
        self,
        base_url: str,
        method: HttpMethod,
        endpoint: str,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        data: dict[str, Any] | None = None,
        files: dict[str, tuple[None, str]] | None = None,
        timeout: httpx.Timeout | None = None,
    ):

        token = await auth_manager.get_access_token()

        headers = headers or {}

        headers["Authorization"] = (
            f"Zoho-oauthtoken {token}"
        )

        endpoint = endpoint if endpoint.startswith("/") else f"/{endpoint}"

        url = f"{base_url}{endpoint}"

        try:
            response = await self.client.request(
                method=method.value,
                url=url,
                headers=headers,
                params=params,
                json=json,
                data=data,
                files=files,
                timeout=timeout
            )

            response.raise_for_status()

            return response.json()

        except httpx.HTTPStatusError as exc:
            detail = exc.response.text

            try:
                detail = json_module.loads(detail)
            except json_module.JSONDecodeError:
                pass

            raise HTTPException(
                status_code=exc.response.status_code,
                detail=detail
            )

        except httpx.RequestError as exc:
            raise HTTPException(
                status_code=503,
                detail=str(exc)
            )

    async def request(
        self,
        method: HttpMethod,
        endpoint: str,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        data: dict[str, Any] | None = None,
        files: dict[str, tuple[None, str]] | None = None,
        timeout: httpx.Timeout | None = None,
    ):

        return await self._request(
            base_url=API_URL,
            method=method,
            endpoint=endpoint,
            params=params,
            json=json,
            headers=headers,
            data=data,
            files=files,
            timeout=timeout
        )

    async def base_request(
        self,
        method: HttpMethod,
        endpoint: str,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        data: dict[str, Any] | None = None,
        files: dict[str, tuple[None, str]] | None = None,
        timeout: httpx.Timeout | None = None,
    ):

        return await self._request(
            base_url=BASE_URL,
            method=method,
            endpoint=endpoint,
            params=params,
            json=json,
            headers=headers,
            data=data,
            files=files,
            timeout=timeout
        )


qntrl_client = QntrlClient()