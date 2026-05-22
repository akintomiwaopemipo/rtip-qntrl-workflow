from fastapi import APIRouter, Depends


from src.services.blueprint_service import (
    BlueprintService,
    MoveCardToNextStagePayload,
    MoveCardToNextStageResponse,
    Transition
)

from src.api.dependencies.qntrl import (
    get_blueprint_service
)


router = APIRouter(
    prefix="/blueprints",
    tags=["Blueprints"]
)


@router.post("/cards/{job_id}/move-to-next-stage")
async def move_card_to_next_stage(
    job_id: str,
    payload: MoveCardToNextStagePayload,
    service: BlueprintService = Depends(
        get_blueprint_service
    )
) -> MoveCardToNextStageResponse:
    return await service.move_card_to_next_stage(job_id, payload)
    

@router.get("/cards/{job_id}/next-transitions")
async def get_next_transitions(
    job_id: str,
    service: BlueprintService = Depends(
        get_blueprint_service
    )
) -> list[Transition]:
    return await service.next_transitions(job_id)



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
