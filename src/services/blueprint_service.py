from typing import Any
from src.domain.api.http_client import HttpMethod
from src.domain.models.app_base_model import AppBaseModel
from src.integrations.qntrl.client import qntrl_client
from src.core.config import settings



layout_id = int(settings.qntrl_layout_id)



class CreateCardPayload(AppBaseModel):
    title: str
    layout_id: int

    record_owner: int | None = None
    team_id: int | None = None
    description: str | None = None
    duedate: str | None = None
    priority: int | None = None

    custom_fields: dict[str, Any] = {}



class Transition(AppBaseModel):
    transition_id: str
    rule_name: str

class TransitionPayload(AppBaseModel):
    transition_id: str


class MoveCardToNextStagePayload(AppBaseModel):
    transition_id: str

class MoveCardToNextStageResponse(AppBaseModel):
    transition_name: str


    
class BlueprintService:

    async def get_all_organizations(self):
        return await qntrl_client.base_request(
            HttpMethod.GET,
            "org"
        )

    async def get_all_layouts(self):
        return await qntrl_client.request(
            HttpMethod.GET,
            "layout"
        )

    async def get_all_blueprints(self):
        
        params = {
            "layout_id": layout_id
        }

        return await qntrl_client.request(
            HttpMethod.GET,
            "/blueprint",
            params=params if params else None
        )
    
    async def next_transitions(self, job_id: str) -> list[Transition]:
        response = await qntrl_client.request(HttpMethod.GET, f"/job/nexttransitions/{job_id}")

        return [
            Transition(
                transition_id=item["transition_id"],
                rule_name=item["transitionrulemap_details"]["businessrule_details"]["rule_name"]
            )
            for item in response
        ]


    async def perform_transition(self, job_id: str, payload: TransitionPayload):

        return await qntrl_client.request(
            HttpMethod.POST,
            f"/job/transition/{job_id}",
            files=payload.multipart()
        )


    async def move_card_to_next_stage(self, job_id: str, payload: MoveCardToNextStagePayload):

        next_transitions = await self.next_transitions(job_id)

        if not next_transitions:
            raise Exception("No transition available")

        transition_id = payload.transition_id

        perform_transition_payload = TransitionPayload(
            transition_id=transition_id
        )

        response = await self.perform_transition(job_id, perform_transition_payload)

        return MoveCardToNextStageResponse(
            transition_name=response["transition_name"]
        )


    async def get_blueprint(
        self,
        blueprint_id: str
    ):
        return await qntrl_client.request(
            HttpMethod.GET,
            f"/blueprints/{blueprint_id}"
        )
    



    async def create_card(
        self,
        payload: CreateCardPayload
    ) -> dict[str, Any]:

        return await qntrl_client.request(
            HttpMethod.POST,
            f"/job",
            files=payload.multipart()
        )


blueprint_service = BlueprintService()
