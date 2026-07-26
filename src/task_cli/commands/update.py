from task_cli.utils.data_service import DataService


def handle_update_task(args):
    ds = DataService()
    tasks = ds.read_tasks()

    task_to_update = next((task for task in tasks if task["id"] == args.id), None)
    if task_to_update is None:
        print("Task not found. Please provide correct ID.")
        return

    task_to_update["description"] = args.description
    ds.write_tasks(tasks)
