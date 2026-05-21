from src.domain.api.api_error import ApiError
from src.domain.submission import CreateBrokerSubmissionPayload, create_broker_submission
from src.services.blueprint_service import CreateCardPayload, blueprint_service, layout_id
from src.api.helpers.humanize_json import humanize_json


class SubmissionWorkflow:

    def __init__(self):
        pass

    async def create_broker_submission(self, payload: CreateBrokerSubmissionPayload):
        
        response = await create_broker_submission(payload)

        if isinstance(response, ApiError):
            raise Exception(f"Failed to create broker submission: {response.status_code} - {response.error}")


        return await blueprint_service.create_card(CreateCardPayload(
            title=f"CaseFile: {response.caseFileVersionId}",
            layout_id=layout_id,
            description=humanize_json(response.model_dump())
        ))
        



submission_workflow = SubmissionWorkflow()