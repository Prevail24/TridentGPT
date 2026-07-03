from core.services.observation_manager import ObservationManager



def new_observation():

    print("\n═══════════════════════════════")
    print("      ⚓ TRIDENTGPT v1.0")
    print("═══════════════════════════════\n")

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

    print("\nObservation Created\n")

    print(observation)