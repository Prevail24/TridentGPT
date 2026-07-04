from dataclasses import dataclass


@dataclass
class Relationship:
    """
    Connects two Entities together.
    """

    id: str

    source: str
    relationship: str
    target: str

    confidence: float = 1.0
    status: str = "active"