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

        for line in lines:
            if line.startswith("- "):
                key, value = line[2:].split(":", 1)
                metadata[key.strip()] = value.strip()

        return Observation(
            id=metadata["ID"],
            type=metadata["Type"],
            title=title,
            author=metadata["Author"],
            created=date.today(),      # temporary
            updated=date.today(),      # temporary
            platform=metadata["Platform"],
            category=metadata["Category"],
            difficulty=metadata["Difficulty"],
            status=metadata["Status"],
        )