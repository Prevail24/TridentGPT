from dataclasses import dataclass
from datetime import date


@dataclass
class Relationship:
    id: str

    source_id: str
    target_id: str

    relation: str

    created: date
    author: str = "Prevail"