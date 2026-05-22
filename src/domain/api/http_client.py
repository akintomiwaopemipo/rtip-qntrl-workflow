from typing import Any, TypeVar
from enum import Enum
import json as json_module

from fastapi import HTTPException
import httpx
from pydantic import BaseModel

from src.api.helpers.multipart import MultipartFiles
from src.domain.api.api_error import ApiError


T = TypeVar("T", bound=BaseModel)


class HttpMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


def nextgen_url(path: str) -> str:
    path = path if path.startswith("/") else f"/{path}"
    return f"http://192.168.103.101:51081/v3/api/v3{path}"


class HttpClient:

    def __init__(
        self,
        timeout: float = 60.0,
        headers: dict[str, str] | None = None,
    ):

        self.timeout = httpx.Timeout(timeout)

        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
        }

        if headers:
            self.headers.update(headers)

    async def request(
        self,
        method: HttpMethod,
        url: str,
        response_model: type[T],
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        files: MultipartFiles | None = None,
        headers: dict[str, str] | None = None,
    ) -> T | ApiError:

        merged_headers = self.headers.copy()

        if headers:
            merged_headers.update(headers)

        # multipart/form-data should not manually set content-type
        if files:
            merged_headers.pop(
                "Content-Type",
                None
            )

        async with httpx.AsyncClient(
            timeout=self.timeout
        ) as client:

            response = await client.request(
                method=method.value,
                url=url,
                params=params,
                json=json,
                data=data,
                files=files,
                headers=merged_headers,
            )

        
        try:
            response.raise_for_status()

            return response_model(
                **response.json()
            )

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


http_client = HttpClient()