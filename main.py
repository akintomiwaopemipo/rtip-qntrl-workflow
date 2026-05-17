from fastapi import FastAPI

from src.api.routes import api_router

app = FastAPI(
    title="Qntrl Enterprise API",
    version="1.0.0"
)


app.include_router(api_router)


@app.get("/health")
async def health():
    return {
        "status": "ok"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)