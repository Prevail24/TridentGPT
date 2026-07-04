from core.services.mission_service import MissionService
from core.services.observation_service import ObservationService
from core.services.evidence_service import EvidenceService
from core.services.entity_service import EntityService

class TridentEngine:
    """
    Central application coordinator for TridentGPT.
    """

    def __init__(self):
        self.observations = ObservationService()
        self.missions = MissionService()
        self.evidence = EvidenceService()
        self.entity = EntityService()