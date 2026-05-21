from fastapi import APIRouter, Depends

from src.api.dependencies.qntrl import get_submission_workflow
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
    return await workflow.create_broker_submission(payload)