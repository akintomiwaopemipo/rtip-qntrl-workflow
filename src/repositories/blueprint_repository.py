from typing import Any

from src.integrations.qntrl.blueprint_client import (
    blueprint_client
)


class BlueprintRepository:

    async def get_all(self):
        return await blueprint_client.get_all_blueprints()

    async def get_by_id(
        self,
        blueprint_id: str
    ):
        return await blueprint_client.get_blueprint(
            blueprint_id
        )

    async def transition(
        self,
        blueprint_id: str,
        payload: dict[str, Any]
    ) -> dict[str, Any]:
        return await blueprint_client.perform_transition(
            blueprint_id,
            payload
        )


blueprint_repository = BlueprintRepository()
