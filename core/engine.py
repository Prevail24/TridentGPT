from core.services.mission_service import MissionService
from core.services.observation_manager import ObservationManager


class TridentEngine:
    """
    Central application coordinator for TridentGPT.
    """

    def __init__(self):
        self.observations = ObservationManager()
        self.missions = MissionService()