import argparse

from cli.commands.dashboard import show_dashboard
from cli.commands.list import list_observations
from cli.commands.mission import new_mission
from cli.commands.new import new_observation
from cli.commands.open import open_observation
from cli.commands.open_mission import open_mission
from cli.commands.evidence import create_evidence
from cli.commands.weaver import analyze_observation



def main():
    parser = argparse.ArgumentParser(
        prog="trident",
        description="TridentGPT - The Watchers Intelligence Platform",
    )

    subparsers = parser.add_subparsers(dest="domain")

    mission_parser = subparsers.add_parser(
        "mission",
        help="Mission commands",
    )
    mission_subparsers = mission_parser.add_subparsers(dest="action")

    mission_subparsers.add_parser(
        "create",
        help="Create a new Mission",
    )

    observation_parser = subparsers.add_parser(
        "observation",
        help="Observation commands",
    )
    
    observation_subparsers = observation_parser.add_subparsers(dest="action")
    
    mission_open_parser = mission_subparsers.add_parser(
        "open",
        help="Open a Mission",
    )

    mission_open_parser.add_argument(
        "mission_id",
        help="Mission ID",
    )

    mission_subparsers.add_parser(
        "list",
        help="List Missions",
    )
    observation_subparsers.add_parser(
        "create",
        help="Create a new Observation",
    )

    observation_subparsers.add_parser(
        "list",
        help="List Observations",
    )

    observation_open_parser = observation_subparsers.add_parser(
        "open",
        help="Open an Observation",
    )

    observation_open_parser.add_argument(
        "observation_id",
        help="Observation ID",
    )

    evidence_parser = subparsers.add_parser(
        "evidence",
        help="Evidence commands",
    )

    weaver_parser = subparsers.add_parser(
        "weaver",
        help="Weaver intelligence commands",
    )

    weaver_subparsers = weaver_parser.add_subparsers(dest="action")

    weaver_analyze_parser = weaver_subparsers.add_parser(
        "analyze",
        help="Analyze an Observation",
    )

    weaver_analyze_parser.add_argument(
        "observation_id",
        help="Observation ID",
    )

    evidence_subparsers = evidence_parser.add_subparsers(dest="action")

    evidence_subparsers.add_parser(
        "create",
        help="Create new Evidence",
    )

    args = parser.parse_args()

    if args.domain == "mission":
        if args.action == "create":
            new_mission()
        elif args.action == "open":
            open_mission(args.mission_id)
        elif args.action == "list":
            list_missions()
        else:
            mission_parser.print_help()

    elif args.domain == "observation":
        if args.action == "create":
            new_observation()
        elif args.action == "list":
            list_observations()
        elif args.action == "open":
            open_observation(args.observation_id)
        else:
            observation_parser.print_help()

    elif args.domain == "evidence":
        if args.action == "create":
            create_evidence()
        else:
            evidence_parser.print_help()
    
    elif args.domain == "weaver":
        if args.action == "analyze":
            analyze_observation(args.observation_id)
        else:
            weaver_parser.print_help()

    else:
        show_dashboard()


if __name__ == "__main__":
    main()