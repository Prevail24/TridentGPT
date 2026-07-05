from core.engine import TridentEngine
from core.rendering.terminal_renderer import TerminalRenderer


def new_mission() -> None:
    renderer = TerminalRenderer()
    renderer.banner("Mission Control")

    title = input("Mission Name   : ").strip()
    mission_type = input("Mission Type   : ").strip()
    objective = input("Objective      : ").strip()
    scope = input("Scope          : ").strip()
    operator = input("Operator       : ").strip() or "Prevail"
    priority = input("Priority       : ").strip() or "normal"

    engine = TridentEngine()

    result = engine.missions.create(
        title=title,
        mission_type=mission_type,
        objective=objective,
        scope=scope,
        operator=operator,
        priority=priority,
    )

    renderer.success(
        "⚓ Mission Established",
        f"""Mission ID

{result.mission.id}

Status

{result.mission.status.upper()}

Workspace

missions/{result.mission.id}/

Saved To

{result.filepath}

Recommended Playbook

TRD-PB-001 Quick Recon""",
    )