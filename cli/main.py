import argparse

from cli.commands.dashboard import show_dashboard
from cli.commands.list import list_missions, list_observations
from cli.commands.mission import new_mission
from cli.commands.new import new_observation
from cli.commands.open import open_observation
from cli.commands.open_mission import open_mission
from cli.commands.evidence import create_evidence
from cli.commands.weaver import analyze_observation
from cli.commands.entity import create_entity, open_entity
from cli.commands.search import search
from cli.commands.relationship import create_relationship, open_relationship
from cli.commands.map import map_mission, map_entity
from cli.commands.analyze import analyze_entity

from core.dashboards.observatory_dashboard import ObservatoryDashboard


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
        "new",
        help="Create a new Mission",
    )

    mission_subparsers.add_parser(
        "create",
        help="Create a new Mission (alias for new)",
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

    map_parser = subparsers.add_parser(
        "map",
        help="Visualize an investigation.",
    )

    map_parser.add_argument(
        "target_type",
        choices=["mission", "entity"],
    )

    map_parser.add_argument(
        "target_id",
        help="Target ID",
    )

    evidence_subparsers = evidence_parser.add_subparsers(dest="action")
    evidence_subparsers.add_parser(
        "create", 
        help="Create new Evidence",
    )

    entity_parser = subparsers.add_parser(
        "entity",
        help="Manage entities.",
    )

    entity_parser.add_argument(
        "action",
        choices=["create", "open"],
    )

    entity_parser.add_argument(
        "entity_id",
        help="Entity ID",
        nargs="?",
    )

    relationship_parser = subparsers.add_parser(
        "relationship",
        help="Manage relationships.",
    )

    relationship_parser.add_argument(
        "action",
        choices=["create", "open"],
    )

    relationship_parser.add_argument(
        "relationship_id",
        nargs="?",
        help="Relationship ID",
    )

    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Run intelligence analysis.",
    )

    analyze_parser.add_argument(
        "target_type",
        choices=["entity"],
    )

    analyze_parser.add_argument(
        "target_id",
    )

    search_parser = subparsers.add_parser(
        "search",
        help="Search The Loom",
    )

    search_parser.add_argument(
        "query",
        help="Search query",
    )

    args = parser.parse_args()

    if args.domain == "mission":
        if args.action in {"new", "create"}:
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

    elif args.domain == "map":
        if args.target_type == "mission":
            map_mission(args.target_id)
        elif args.target_type == "entity":
            map_entity(args.target_id)

    elif args.domain == "entity":
        if args.action == "create":
            create_entity()
        elif args.action == "open":
            open_entity(args.entity_id)
        else:
            entity_parser.print_help()

    elif args.domain == "search":
        search(args.query)

    elif args.domain == "relationship":
        if args.action == "create":
            create_relationship()
        elif args.action == "open":
            open_relationship(args.relationship_id)
        else:
            relationship_parser.print_help()


    else:
        ObservatoryDashboard().show()

if __name__ == "__main__":
    main()