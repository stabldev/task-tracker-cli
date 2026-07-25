import argparse

from task_cli.commands.add import handle_add_task


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add new task.")
    add_parser.add_argument("description", type=str, help="Description of the task.")
    add_parser.set_defaults(func=handle_add_task)

    args = parser.parse_args()
    args.func(args)
