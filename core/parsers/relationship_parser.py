from core.models.relationship import Relationship


class RelationshipParser:
    """
    Converts Relationship markdown into a Relationship object and back.
    """

    def parse(self, markdown: str) -> Relationship:

        metadata = {}

        for line in markdown.splitlines():

            line = line.strip()

            if not line.startswith("- "):
                continue

            item = line[2:]

            if ":" not in item:
                continue

            key, value = item.split(":", 1)

            metadata[key.strip()] = value.strip()

        return Relationship(
            id=metadata["ID"],
            source=metadata["Source"],
            relationship=metadata["Relationship"],
            target=metadata["Target"],
            confidence=float(metadata.get("Confidence", 1.0)),
            status=metadata.get("Status", "active"),
        )

    def serialize(self, relationship: Relationship) -> str:

        return f"""# {relationship.id}

## Metadata

- ID: {relationship.id}
- Source: {relationship.source}
- Relationship: {relationship.relationship}
- Target: {relationship.target}
- Confidence: {relationship.confidence}
- Status: {relationship.status}

---

# Notes

"""