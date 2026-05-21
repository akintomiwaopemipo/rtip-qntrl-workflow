from fastapi.responses import JSONResponse
from pydantic import BaseModel


class ErrorMessage(BaseModel):
    error: str


def error_response(
    exception: Exception,
    status_code: int = 400,
) -> JSONResponse:

    return JSONResponse(
        status_code=status_code,
        content=ErrorMessage(
            error=str(exception)
        ).model_dump()
    )