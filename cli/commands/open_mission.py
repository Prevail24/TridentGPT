from core.engine import TridentEngine
from core.renderers.mission_renderer import MissionRenderer


def open_mission(mission_id: str):
    engine = TridentEngine()

    mission = engine.missions.open(mission_id)

    MissionRenderer().render(mission)