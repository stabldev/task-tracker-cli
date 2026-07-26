from pprint import pprint

from task_cli.utils.data_service import DataService


def handle_list_tasks(args):
    ds = DataService()
    tasks = ds.read_tasks()

    match args.status:
        case "todo":
            result = [task for task in tasks if task["status"] == "todo"]
        case "done":
            result = [task for task in tasks if task["status"] == "done"]
        case "in-progress":
            result = [task for task in tasks if task["status"] == "in-progress"]
        case _:
            result = tasks[:]

    pprint(result)
