import json
from collections.abc import Iterable
from pathlib import Path
from typing import Unpack

from task_cli.utils.types import Task, TaskUpdate


class DataService:
    def __init__(self):
        self.data_path = Path.cwd() / "data.json"
        if not self.data_path.exists():
            self.data_path.write_text(json.dumps([]))

    def read_tasks(self) -> list[Task]:
        with open(self.data_path) as file:
            data = file.read()

        return [Task.from_dict(item) for item in json.loads(data)]

    def write_tasks(self, tasks: Iterable[Task]) -> None:
        tasks_data = [task.to_dict() for task in tasks]
        with open(self.data_path, "w", encoding="utf-8") as file:
            json.dump(tasks_data, file, default=str, indent=2)

    def update_task(self, id: int, **kwargs: Unpack[TaskUpdate]) -> None:
        tasks = self.read_tasks()
        task_to_update = next((task for task in tasks if task.id == id), None)

        if task_to_update is None:
            raise RuntimeError("Task not found. Please provide correct ID.")

        task_to_update.update(**kwargs)
        self.write_tasks(tasks)
