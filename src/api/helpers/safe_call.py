from collections.abc import Awaitable, Callable
from typing import Any

from src.api.helpers.error_response import error_response


async def safe_call(
    handler: Callable[[], Awaitable[Any]],
    status_code: int = 400,
):

    try:

        return await handler()

    except Exception as e:

        return error_response(
            e,
            status_code
        )