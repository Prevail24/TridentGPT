from core.rendering.terminal_renderer import TerminalRenderer
from core.engine import TridentEngine


def list_observations():
    renderer = TerminalRenderer()
    renderer.banner("Observation Archive")
    engine = TridentEngine()
    observations = engine.observations.list()
    renderer.archive(observations)

def list_missions():
        renderer = TerminalRenderer()
        renderer.banner("Mission Archive")
        engine = TridentEngine()
        missions = engine.missions.list()

        if not missions:
            renderer.info("No Missions Found", "Create one with: trident mission new")
            return

        renderer.archive(missions)    