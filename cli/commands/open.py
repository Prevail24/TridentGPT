from core.services.observation_manager import ObservationManager


def open_observation(observation_id: str):
    manager = ObservationManager()
    content = manager.open(observation_id)

    print()
    print(content)