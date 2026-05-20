from typing import Any
from pydantic import BaseModel
from src.integrations.qntrl.client import qntrl_client
from src.core.config import settings



layout_id = int(settings.qntrl_layout_id)



class CreateCardPayload(BaseModel):
    title: str
    layout_id: int

    record_owner: int | None = None
    team_id: int | None = None
    description: str | None = None
    duedate: str | None = None
    priority: int | None = None

    custom_fields: dict[str, Any] = {}



    
class BlueprintService:

    async def get_all_organizations(self):
        return await qntrl_client.base_request(
            "GET",
            "org"
        )

    async def get_all_layouts(self):
        return await qntrl_client.request(
            "GET",
            "layout"
        )

    async def get_all_blueprints(self):
        
        params = {
            "layout_id": layout_id
        }

        return await qntrl_client.request(
            "GET",
            "/blueprint",
            params=params if params else None
        )

    async def get_blueprint(
        self,
        blueprint_id: str
    ):
        return await qntrl_client.request(
            "GET",
            f"/blueprints/{blueprint_id}"
        )
    
    async def get_transitions(
        self,
        blueprint_id: str
    ):
        return await qntrl_client.request(
            "GET",
            f"/blueprints/{blueprint_id}/transitions"
        )

    async def perform_transition(
        self,
        blueprint_id: str,
        payload: dict[str, Any]
    ) -> dict[str, Any]:
        return await qntrl_client.request(
            "POST",
            f"/blueprints/{blueprint_id}/transitions",
            json=payload
        )



    async def create_card(
        self,
        payload: CreateCardPayload
    ) -> dict[str, Any]:

        print(f"Creating card with payload: {payload.model_dump()}")

        return await qntrl_client.request(
            "POST",
            f"/job",
            json=payload.model_dump()
        )


blueprint_service = BlueprintService()
