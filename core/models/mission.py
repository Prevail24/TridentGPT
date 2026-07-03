from dataclasses import dataclass, field
from datetime import date


@dataclass
class Mission:
    """
    A Mission represents a larger operation that can contain many Observations.
    """

    id: str
    title: str
    mission_type: str
    priority: str
    observer: str
    created: date
    updated: date
    status: str = "active"

    observations: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)

    def add_observation(self, observation_id: str):
        if observation_id not in self.observations:
            self.observations.append(observation_id)

    def complete(self):
        self.status = "completed"
        self.updated = date.today()