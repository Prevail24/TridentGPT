import argparse

from cli.commands.dashboard import show_dashboard
from cli.commands.list import list_observations
from cli.commands.mission import new_mission
from cli.commands.new import new_observation
from cli.commands.open import open_observation


def main():
    parser = argparse.ArgumentParser(
        prog="trident",
        description="TridentGPT - The OSINT Investigation Engine"
    )

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser(
        "new",
        help="Create a new Observation"
    )

    subparsers.add_parser(
        "list",
        help="List Observations"
    )

    subparsers.add_parser(
        "mission",
        help="Create a new Mission"
    )

    open_parser = subparsers.add_parser(
        "open",
        help="Open an Observation"
    )

    open_parser.add_argument(
        "observation_id",
        help="Observation ID"
    )

    args = parser.parse_args()

    if args.command == "new":
        new_observation()
    elif args.command == "list":
        list_observations()
    elif args.command == "open":
        open_observation(args.observation_id)
    elif args.command == "mission":
        new_mission()
    else:
        show_dashboard()


if __name__ == "__main__":
    main()