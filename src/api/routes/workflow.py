from fastapi import APIRouter, Depends

from src.api.dependencies.qntrl import get_submission_workflow
from src.api.helpers.safe_call import safe_call
from src.domain.submission import CreateBrokerSubmissionPayload
from src.workflows.submission import SubmissionWorkflow


router = APIRouter(
    prefix="/workflows",
    tags=["Workflows"]
)


@router.post("/broker-submission")
async def create_broker_submission(
    payload: CreateBrokerSubmissionPayload,
    workflow: SubmissionWorkflow = Depends(
        get_submission_workflow
    )
):
    return await safe_call(
        lambda: workflow.create_broker_submission(payload)
    )