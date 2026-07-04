from datetime import date

from core.models.observation import Observation


class ObservationParser:

    def parse(self, markdown: str) -> Observation:
        """
        Convert markdown into an Observation.
        """

        lines = markdown.splitlines()

        title = lines[0].replace("# ", "").strip()

        metadata = {}
        evidence = []
        notes = []

        current_section = None

        for line in lines:
            stripped = line.strip()

            if stripped == "# Evidence":
                current_section = "evidence"
                continue

            if stripped == "# Notes":
                current_section = "notes"
                continue

            if stripped.startswith("# "):
                current_section = None
                continue

            if not stripped.startswith("- "):
                continue

            item = stripped[2:].strip()

            if current_section == "evidence":
                if item:
                    evidence.append(item)
                continue

            if current_section == "notes":
                if item:
                    notes.append(item)
                continue

            if ":" not in item:
                continue

            key, value = item.split(":", 1)
            metadata[key.strip()] = value.strip()

        return Observation(
            id=metadata["ID"],
            type=metadata["Type"],
            title=title,
            author=metadata["Author"],
            created=date.today(),
            updated=date.today(),
            platform=metadata["Platform"],
            category=metadata["Category"],
            difficulty=metadata["Difficulty"],
            status=metadata["Status"],
            mission_id=metadata.get("Mission") or None,
            evidence=evidence,
            notes=notes,
        )