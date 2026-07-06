from core.repositories.observation_repository import ObservationRepository
from core.services.observation_engine import ObservationEngine


repo = ObservationRepository()
engine = ObservationEngine()

observation = repo.list()[-1]

entities = engine.process(observation)

print()
print("Observation Processed")
print("---------------------")
print(f"Observation: {observation.id}")
print(f"Category: {observation.category}")
print()

for entity in entities:
    print(f"{entity.id} | {entity.entity_type} | {entity.value}")

print()