from pathlib import Path


def list_observations():
    observations_root = Path("knowledge/observations")

    print("\n═══════════════════════════════")
    print("      ⚓ TRIDENTGPT v1.0")
    print("═══════════════════════════════\n")

    print("Observation Archive")
    print("-------------------")

    if not observations_root.exists():
        print("No observations found.")
        return

    observations = sorted(observations_root.glob("*/OBS-*.md"))

    if not observations:
        print("No observations found.")
        return

    for observation in observations:
        print(f"- {observation.stem}")