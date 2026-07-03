from dataclasses import dataclass, field
from datetime import date

from core.models.thread import Thread


@dataclass
class Observation(Thread):
    """
    An Observation represents an active or completed investigation.
    """

    platform: str = ""
    category: str = ""
    difficulty: str = ""
    status: str = "active"

    evidence: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    pivots: list[str] = field(default_factory=list)
    hypotheses: list[str] = field(default_factory=list)
    dead_ends: list[str] = field(default_factory=list)

    def add_evidence(self, item: str):
        self.evidence.append(item)

    def add_note(self, note: str):
        self.notes.append(note)

    def add_pivot(self, pivot: str):
        self.pivots.append(pivot)

    def add_hypothesis(self, hypothesis: str):
        self.hypotheses.append(hypothesis)

    def add_dead_end(self, dead_end: str):
        self.dead_ends.append(dead_end)