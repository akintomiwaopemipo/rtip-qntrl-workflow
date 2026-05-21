from typing import Any

from src.domain.api.http_client import HttpMethod, http_client, nextgen_url
from src.domain.models.app_base_model import AppBaseModel


class BrokerSubmissionResponse(AppBaseModel):
    brokerVersionId: str
    caseFileVersionId: str

    error: str
    filingFee: float | int

    guidelinesViolations: list[Any]

    message: str

    policyFee: float | int
    premium: float | int
    sltax: float | int

    submissionStatus: str

    totalDue: float | int
    totaltax: float | int


class CreateBrokerSubmissionPayload(AppBaseModel):
    buildingAddress: dict[str, Any]
    insuranceTerms: dict[str, Any]
    buildingAttributes: dict[str, Any]
    submissionDetails: dict[str, Any]


async def create_broker_submission(payload: CreateBrokerSubmissionPayload):


    return await http_client.request(
        method = HttpMethod.POST,
        url = nextgen_url("/brokersubmission"),
        response_model = BrokerSubmissionResponse,
        json = payload.model_dump()
    )