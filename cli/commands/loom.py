from core.services.loom_service import LoomService


def show_loom(entity_value: str):
    loom = LoomService()

    result = loom.graph_for_entity(entity_value)

    if result is None:
        print("Entity not found.")
        return

    entity, graph = result

    print()
    print("═══════════════════════════════")
    print("          THE LOOM")
    print("═══════════════════════════════")
    print()

    print(f"{entity.entity_type.upper()}")
    print(f"{entity.value}")
    print()

    if not graph:
        print("No relationships.")
        return

    print("Relationships")
    print("-------------")

    for relationship_type, targets in graph.items():
        print(f"{relationship_type}")

        for target in targets:
            if target is None:
                continue

            print(
                f"  -> {target.entity_type}: {target.value}"
            )

        print()