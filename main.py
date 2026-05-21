from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging
from src.api.helpers.error_response import ErrorMessage
from src.api.routes import api_router

app = FastAPI(
    title="Qntrl Enterprise API",
    version="1.0.0"
)

logger = logging.getLogger(__name__)


app.include_router(api_router)

@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception,
):

    logger.exception(exc)

    return JSONResponse(
        status_code=400,
        content=ErrorMessage(
            error=str(exc),
        ).model_dump()
    )


@app.get("/health")
async def health():
    return {
        "status": "ok"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)