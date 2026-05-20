from fastapi import APIRouter, Depends

from src.api.dependencies.qntrl import get_submission_workflow
from src.workflows.submission import SubmissionWorkflow


router = APIRouter(
    prefix="/workflows",
    tags=["Workflows"]
)


@router.post("/broker-submission")
async def create_broker_submission(
    workflow: SubmissionWorkflow = Depends(
        get_submission_workflow
    )
):
    return await workflow.create_broker_submission()