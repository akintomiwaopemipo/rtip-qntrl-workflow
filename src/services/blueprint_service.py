from typing import Any

from src.domain.blueprint.service import (
    domain_blueprint_service
)

from src.integrations.qntrl.client import qntrl_client

class BlueprintService:

    async def get_all_organizations(self):
        return await qntrl_client.base_request("GET","org")

    async def get_all_blueprints(self):
        return await (
            domain_blueprint_service
            .list_blueprints()
        )

    async def get_blueprint(
        self,
        blueprint_id: str
    ):
        return await (
            domain_blueprint_service
            .get_blueprint(blueprint_id)
        )

    async def perform_transition(
        self,
        blueprint_id: str,
        payload: dict[str, Any]
    ) -> dict[str, Any]:
        return await (
            domain_blueprint_service
            .transition(
                blueprint_id,
                payload
            )
        )


blueprint_service = BlueprintService()
