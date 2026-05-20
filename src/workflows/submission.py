from typing import cast

from src.domain.submission import BrokerSubmissionResponse, create_broker_submission
from src.services.blueprint_service import CreateCardPayload, blueprint_service, layout_id
from src.utils.humanize_json import humanize_json


class SubmissionWorkflow:

    def __init__(self):
        pass

    async def create_broker_submission(self):
        
        response = cast(BrokerSubmissionResponse, await create_broker_submission())

        return await blueprint_service.create_card(CreateCardPayload(
            title=f"#{response.caseFileVersionId}",
            layout_id=layout_id,
            description=humanize_json(response.model_dump())
        ))
        



submission_workflow = SubmissionWorkflow()