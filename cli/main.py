import argparse

from cli.commands.new import new_observation


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

    args = parser.parse_args()

    if args.command == "new":
        new_observation()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()