from pathlib import Path

from core.config import Config
from core.models.relationship import Relationship
from core.parsers.relationship_parser import RelationshipParser


class RelationshipRepository:
    """
    Handles persistence for Relationship objects.
    """

    def __init__(self):
        self.parser = RelationshipParser()

    def save(self, relationship: Relationship) -> Path:
        year = relationship.id.split("-")[1]

        relationship_root = (
            Config.KNOWLEDGE_DIR
            / "relationships"
            / year
        )

        relationship_root.mkdir(parents=True, exist_ok=True)

        filepath = relationship_root / f"{relationship.id}.md"

        markdown = self.parser.serialize(relationship)
        filepath.write_text(markdown, encoding="utf-8")

        return filepath

    def open(self, relationship_id: str) -> Relationship:
        """
        Return one Relationship object by ID.
        """
        year = relationship_id.split("-")[1]

        filepath = (
            Config.KNOWLEDGE_DIR
            / "relationships"
            / year
            / f"{relationship_id}.md"
        )

        markdown = filepath.read_text(encoding="utf-8")

        return self.parser.parse(markdown)

    def list(self) -> list[Relationship]:
        """
        Return all Relationship objects stored in The Loom.
        """
        relationship_root = Config.KNOWLEDGE_DIR / "relationships"

        relationship_items = []

        for file in sorted(relationship_root.glob("**/*.md")):
            relationship_items.append(self.open(file.stem))

        return relationship_items