from core.services.entity_resolver import EntityResolver


class ObservationEngine:
    """
    Converts canonical observations into entities.
    """

    def __init__(self):
        self.entities = EntityResolver()

    def process(self, observation):
        resolved = []

        if observation.category == "port":
            host = self.entities.resolve(
                "host",
                observation.data["host"],
            )

            service = self.entities.resolve(
                "service",
                observation.data.get("service", "unknown"),
            )

            resolved.extend([host, service])

        return resolved