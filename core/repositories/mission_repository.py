from core.config import Config
from core.parsers.mission_parser import MissionParser


class MissionRepository:
    def __init__(self):
        self.parser = MissionParser()

    def open(self, mission_id: str):
        year = mission_id.split("-")[1]
        filepath = Config.KNOWLEDGE_DIR / "missions" / year / f"{mission_id}.md"
        markdown = filepath.read_text(encoding="utf-8")
        return self.parser.parse(markdown)

    def list(self):
        missions_root = Config.KNOWLEDGE_DIR / "missions"
        missions = []

        for file in sorted(missions_root.glob("**/*.md")):
            missions.append(self.open(file.stem))

        return missions