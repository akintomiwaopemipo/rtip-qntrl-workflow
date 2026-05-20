from fastapi import APIRouter, Depends

from src.schemas.blueprint import (
    TransitionPayload
)

from src.services.blueprint_service import (
    BlueprintService
)

from src.api.dependencies.qntrl import (
    get_blueprint_service
)


router = APIRouter(
    prefix="/blueprints",
    tags=["Blueprints"]
)


@router.get("/organizations")
async def get_all_organizations(
    service: BlueprintService = Depends(
        get_blueprint_service
    )
):
    return await service.get_all_organizations()


@router.get("/layouts")
async def get_all_layouts(
    service: BlueprintService = Depends(
        get_blueprint_service
    )
):
    return await service.get_all_layouts()



@router.get("/")
async def get_all_blueprints(
    service: BlueprintService = Depends(
        get_blueprint_service
    )
):
    return await service.get_all_blueprints()


@router.get("/{blueprint_id}")
async def get_blueprint(
    blueprint_id: str,
    service: BlueprintService = Depends(
        get_blueprint_service
    )
):
    return await service.get_blueprint(
        blueprint_id
    )


@router.post("/{blueprint_id}/transitions")
async def perform_transition(
    blueprint_id: str,
    payload: TransitionPayload,
    service: BlueprintService = Depends(
        get_blueprint_service
    )
):
    return await service.perform_transition(
        blueprint_id,
        payload.model_dump()
    )
