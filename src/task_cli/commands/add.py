from datetime import UTC, datetime

from task_cli.utils.data_service import DataService
from task_cli.utils.types import Task


def handle_add_task(args) -> None:
    ds = DataService()
    tasks_list = ds.read_tasks()

    new_task = Task(
        id=max((task.id for task in tasks_list), default=0) + 1,
        description=args.description,
        status="todo",
        created_at=datetime.now(UTC),
        updated_at=datetime.now(UTC),
    )

    tasks_list.append(new_task)
    ds.write_tasks(tasks_list)

    print(f"Task added successfully: {new_task.id}")
