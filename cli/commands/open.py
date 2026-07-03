from core.rendering.terminal_renderer import TerminalRenderer
from core.services.observation_manager import ObservationManager


def open_observation(observation_id: str):
    renderer = TerminalRenderer()
    renderer.banner("Open Observation")

    manager = ObservationManager()
    observation = manager.open(observation_id)

    renderer.observation_card(observation)