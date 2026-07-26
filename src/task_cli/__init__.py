import argparse

from task_cli.commands.add import handle_add_task
from task_cli.commands.delete import handle_delete_task
from task_cli.commands.mark_done import handle_mark_done_task
from task_cli.commands.mark_in_progress import handle_mark_in_progress_task
from task_cli.commands.update import handle_update_task


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    # "add" command
    add_parser = subparsers.add_parser("add", help="Add new task.")
    add_parser.add_argument("description", type=str, help="Description of the task.")
    add_parser.set_defaults(func=handle_add_task)

    # "update" command
    update_parser = subparsers.add_parser("update", help="Update a task.")
    update_parser.add_argument("id", type=int, help="ID of the task.")
    update_parser.add_argument(
        "description", type=str, help="New description of the task."
    )
    update_parser.set_defaults(func=handle_update_task)

    # "delete" command
    delete_parser = subparsers.add_parser("delete", help="Delete a task.")
    delete_parser.add_argument("id", type=int, help="ID of the task.")
    delete_parser.set_defaults(func=handle_delete_task)

    # "mark-in-progress" command
    mark_in_progress_parser = subparsers.add_parser(
        "mark-in-progress", help="Mark a task as in progress."
    )
    mark_in_progress_parser.add_argument("id", type=int, help="ID of the task.")
    mark_in_progress_parser.set_defaults(func=handle_mark_in_progress_task)

    # "mark-done" command
    mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done.")
    mark_done_parser.add_argument("id", type=int, help="ID of the task.")
    mark_done_parser.set_defaults(func=handle_mark_done_task)

    args = parser.parse_args()
    args.func(args)
