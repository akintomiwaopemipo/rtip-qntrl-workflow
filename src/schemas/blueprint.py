from typing import Any
from pydantic import BaseModel


class TransitionPayload(BaseModel):
    transition_id: str
    card_id: str
    fields: dict[str, Any] = {}


class GenericResponse(BaseModel):
    data: Any
