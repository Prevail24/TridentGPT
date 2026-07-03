from core.engine import TridentEngine
from core.rendering.terminal_renderer import TerminalRenderer


def new_mission():

    renderer = TerminalRenderer()
    renderer.banner("Mission Control")

    title = input("Operation Name : ")
    mission_type = input("Mission Type  : ")
    priority = input("Priority      : ")

    engine = TridentEngine()

    result = engine.missions.create(
        title=title,
        mission_type=mission_type,
        priority=priority,
    )

    renderer.success(
        "⚓ Mission Established",
        f"""Mission ID

{result.mission.id}

Status

{result.mission.status.upper()}

Saved To

{result.filepath}""",
    )