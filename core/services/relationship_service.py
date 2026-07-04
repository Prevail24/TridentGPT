from datetime import date

from core.models.relationship import Relationship
from core.repositories.relationship_repository import RelationshipRepository


class RelationshipService:
    """
    Creates and manages links between objects in The Loom.
    """

    def __init__(self):
        self.repository = RelationshipRepository()

    def link(
        self,
        source_id: str,
        target_id: str,
        relation: str,
        author: str = "Prevail",
    ) -> Relationship:
        relationship = Relationship(
            id="REL-TEMP",
            source_id=source_id,
            target_id=target_id,
            relation=relation,
            created=date.today(),
            author=author,
        )

        return relationship