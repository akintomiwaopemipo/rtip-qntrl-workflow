from fastapi.responses import JSONResponse
from pydantic import BaseModel


class ErrorMessage(BaseModel):
    detail: str


def error_response(
    exception: Exception,
    status_code: int = 400,
) -> JSONResponse:

    return JSONResponse(
        status_code=status_code,
        content=ErrorMessage(
            detail=str(exception)
        ).model_dump()
    )