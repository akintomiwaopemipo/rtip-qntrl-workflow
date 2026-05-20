from fastapi import APIRouter

from src.api.routes.workflow import router as workflow_router
from src.api.routes.blueprint import router as blueprint_router
from src.api.routes.oauth import router as oauth_router

api_router = APIRouter()

api_router.include_router(workflow_router)
api_router.include_router(blueprint_router)
api_router.include_router(oauth_router)