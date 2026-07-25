import json
from datetime import UTC, datetime

from task_cli.utils.data_service import DataService
from task_cli.utils.types import Task


def handle_add_task(args) -> None:
    ds = DataService()
    tasks_list = [Task(**item) for item in json.loads(ds.read())]

    new_task = Task(
        id=len(tasks_list) + 1,
        description=args.description,
        status="todo",
        created_at=datetime.now(UTC),
        updated_at=datetime.now(UTC),
    )

    tasks_list.append(new_task)
    tasks_list_str = json.dumps(tasks_list, default=str, indent=2)
    ds.write(tasks_list_str)

    print(f"Task added successfully: {new_task['id']}")
