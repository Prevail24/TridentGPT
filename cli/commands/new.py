from core.rendering.terminal_renderer import TerminalRenderer
from core.services.observation_manager import ObservationManager


def new_observation():
    renderer = TerminalRenderer()
    renderer.banner("Create New Observation")

    title = input("Challenge Name : ")
    platform = input("Platform       : ")
    category = input("Category       : ")
    difficulty = input("Difficulty     : ")

    manager = ObservationManager()

    observation = manager.create(
        title=title,
        platform=platform,
        category=category,
        difficulty=difficulty,
    )

    renderer.success("Thread successfully woven.")
    renderer.observation_card(observation)