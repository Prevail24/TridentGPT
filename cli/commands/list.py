from core.rendering.terminal_renderer import TerminalRenderer
from core.services.observation_manager import ObservationManager


def list_observations():
    renderer = TerminalRenderer()
    renderer.banner("Observation Archive")

    manager = ObservationManager()

    observations = manager.list()

    renderer.archive(observations)