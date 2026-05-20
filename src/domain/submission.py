from typing import Any

import httpx
from pydantic import BaseModel


class BrokerSubmissionResponse(BaseModel):
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




async def create_broker_submission() -> BrokerSubmissionResponse | dict[str, Any]:
   
    url = "http://192.168.103.101:51081/v3/api/v3/brokerSubmission"

    payload = {
        "buildingAddress": {
            "city": "Oviedo",
            "postalCode": "32765",
            "stateProvince": "FL",
            "street1": "1201 allendale dr",
            "street2": ""
        },
        "insuranceTerms": {
            "buildingDeductible": 10000,
            "timeElementLimit": 20000,
            "contentsDeductible": 0,
            "buildingLimit": 300000,
            "contentsLimit": 0
        },
        "buildingAttributes": {
            "contentsRcv": 0,
            "timeElementValue": 20000,
            "basementPresence": "NO",
            "occupancy": "Single-Family: Permanent Dwelling",
            "buildingRcv": 310000,
            "construction": "Wood Frame",
            "buildingArea": 2400,
            "yearBuilt": 2000,
            "numberOfStories": 2
        },
        "submissionDetails": {
            "brokerId": "05bfb8c3afc05000_001",
            "namedInsuredEmail": "j@gmail.com",
            "mailingAddress": {
                "city": "Oviedo",
                "postalCode": "32765",
                "stateProvince": "FL",
                "street1": "1201 allendale dr",
                "street2": ""
            },
            "inceptionDate": "2023-01-15",
            "namedInsured": "Jane Doe"
        }
    }

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    timeout = httpx.Timeout(
        connect=10.0,
        read=60.0,
        write=30.0,
        pool=10.0
    )

    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(
                url,
                json=payload,
                headers=headers,
            )

            response.raise_for_status()

            return BrokerSubmissionResponse(**response.json())

    except httpx.ReadTimeout:
        return {
            "error": "Upstream API timed out"
        }

    except httpx.HTTPStatusError as e:
        return {
            "status_code": e.response.status_code,
            "response": e.response.text
        }