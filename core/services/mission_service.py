from datetime import date
from pathlib import Path

from core.config import Config
from core.models.mission import Mission
from core.parsers.mission_parser import MissionParser


class CreateMissionResult:
    def __init__(self, mission: Mission, filepath: str, success: bool = True):
        self.mission = mission
        self.filepath = filepath
        self.success = success


class MissionService:
    def create(
        self,
        title: str,
        mission_type: str,
        priority: str,
        observer: str = "Prevail",
    ) -> CreateMissionResult:
        mission_id = self._generate_id()

        mission = Mission(
            id=mission_id,
            title=title,
            mission_type=mission_type,
            priority=priority,
            observer=observer,
            created=date.today(),
            updated=date.today(),
        )

        filepath = self._save(mission)

        return CreateMissionResult(
            mission=mission,
            filepath=str(filepath),
        )

    def open(self, mission_id: str) -> Mission:
        year = mission_id.split("-")[1]
        filepath = Config.KNOWLEDGE_DIR / "missions" / year / f"{mission_id}.md"

        markdown = filepath.read_text(encoding="utf-8")

        parser = MissionParser()
        return parser.parse(markdown)

    def save(self, mission: Mission) -> Path:
        return self._save(mission)

    def add_observation(self, mission_id: str, observation_id: str):
        mission = self.open(mission_id)
        mission.add_observation(observation_id)
        self.save(mission)

    def _generate_id(self) -> str:
        year = date.today().year
        missions_root = Config.KNOWLEDGE_DIR / "missions" / str(year)
        missions_root.mkdir(parents=True, exist_ok=True)

        existing = sorted(missions_root.glob(f"MIS-{year}-*.md"))
        number = len(existing) + 1

        return f"MIS-{year}-{number:04d}"

    def _save(self, mission: Mission) -> Path:
        year = mission.created.year
        missions_root = Config.KNOWLEDGE_DIR / "missions" / str(year)
        missions_root.mkdir(parents=True, exist_ok=True)

        filepath = missions_root / f"{mission.id}.md"

        observations = "\n".join(
            f"- {obs_id}"
            for obs_id in mission.observations
        )

        content = f"""# {mission.title}

## Metadata

- ID: {mission.id}
- Type: Mission
- Mission Type: {mission.mission_type}
- Priority: {mission.priority}
- Observer: {mission.observer}
- Status: {mission.status}

---

# Observations

{observations}
"""

        filepath.write_text(content, encoding="utf-8")
        return filepath