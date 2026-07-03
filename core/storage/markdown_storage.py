from pathlib import Path

from core.models.observation import Observation


class MarkdownStorage:
    """
    Saves and loads Observations from The Loom.
    """

    def save(self, observation: Observation) -> Path:
        year = observation.created.year
        folder = Path(f"knowledge/observations/{year}")
        folder.mkdir(parents=True, exist_ok=True)
        filepath = folder / f"{observation.id}.md"
        content = f"""# {observation.title}

## Metadata

- ID: {observation.id}
- Type: {observation.type}
- Author: {observation.author}
- Platform: {observation.platform}
- Category: {observation.category}
- Difficulty: {observation.difficulty}
- Status: {observation.status}

---

# Notes

"""

        filepath.write_text(content, encoding="utf-8")

        return filepath

    def load(self, observation_id: str) -> str:
        """
        Loads a raw Observation markdown file.
        """

        observations_root = Path("knowledge/observations")

        matches = list(observations_root.glob(f"**/{observation_id}.md"))

        if not matches:
            raise FileNotFoundError(
                f"Observation '{observation_id}' was not found."
            )

        return matches[0].read_text(encoding="utf-8")