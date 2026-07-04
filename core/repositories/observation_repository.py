from core.storage.markdown_storage import MarkdownStorage
from core.parsers.observation_parser import ObservationParser


class ObservationRepository:
    """
    Handles persistence for Observation objects.
    """

    def __init__(self):
        self.storage = MarkdownStorage()
        self.parser = ObservationParser()

    def save(self, observation):
        return self.storage.save(observation)

    def open(self, observation_id: str):
        markdown = self.storage.load(observation_id)
        return self.parser.parse(markdown)

    def list(self):
        markdown_files = self.storage.list()

        observations = []

        for markdown in markdown_files:
            try:
                observations.append(self.parser.parse(markdown))
            except KeyError:
                continue

        return observations