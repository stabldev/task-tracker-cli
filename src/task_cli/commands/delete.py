from task_cli.utils.data_service import DataService


def handle_delete_task(args):
    ds = DataService()
    tasks = ds.read_tasks()

    task_to_delete = next((task for task in tasks if task["id"] == args.id), None)
    if task_to_delete is None:
        print("Task not found. Please provide correct ID.")
        return

    tasks.remove(task_to_delete)
    ds.write_tasks(tasks)
    print("success")
