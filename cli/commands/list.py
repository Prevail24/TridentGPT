from core.rendering.terminal_renderer import TerminalRenderer
from core.engine import TridentEngine


def list_observations():
    renderer = TerminalRenderer()
    renderer.banner("Observation Archive")

    engine = TridentEngine()

    observations = engine.observations.list()

    renderer.archive(observations)