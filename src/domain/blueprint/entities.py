from dataclasses import dataclass
from typing import Any


@dataclass
class Blueprint:
    id: str
    name: str
    raw: Any
