from typing import Any

from src.repositories.blueprint_repository import (
    blueprint_repository
)


class DomainBlueprintService:

    async def list_blueprints(self):
        return await blueprint_repository.get_all()

    async def get_blueprint(
        self,
        blueprint_id: str
    ):
        return await blueprint_repository.get_by_id(
            blueprint_id
        )

    async def transition(
        self,
        blueprint_id: str,
        payload: dict[str, Any]
    ) -> dict[str, Any]:
        return await blueprint_repository.transition(
            blueprint_id,
            payload
        )


domain_blueprint_service = (
    DomainBlueprintService()
)
