from datetime import date

from core.models.observation import Observation
from core.storage.markdown_storage import MarkdownStorage
from core.services.id_generator import IDGenerator


class ObservationManager:
    """
    Coordinates the creation and management of Observations.
    """

    def create(
        self,
        title: str,
        platform: str,
        category: str,
        difficulty: str,
        author: str = "Prevail",
    ) -> Observation:

        generator = IDGenerator()
        observation_id = generator.generate("OBS")

        observation = Observation(
            id=observation_id,
            type="Observation",
            title=title,
            author=author,
            created=date.today(),
            updated=date.today(),
            platform=platform,
            category=category,
            difficulty=difficulty,
        )

        storage = MarkdownStorage()
        filepath = storage.save(observation)

        return observation
    
    def open(self, observation_id: str) -> str:
        storage = MarkdownStorage()

        return storage.load(observation_id)   