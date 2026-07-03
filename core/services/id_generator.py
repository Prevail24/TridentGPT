from datetime import date
from pathlib import Path


class IDGenerator:
    """
    Generates sequential IDs for The Watchers.
    """

    def generate(self, prefix: str) -> str:

        year = date.today().year
        folder = Path(f"knowledge/observations/{year}")
        folder.mkdir(parents=True, exist_ok=True)
        existing = sorted(folder.glob(f"{prefix}-{year}-*.md"))
        number = len(existing) + 1

        return f"{prefix}-{year}-{number:04d}"