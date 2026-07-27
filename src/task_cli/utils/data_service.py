import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Unpack

from pydantic import TypeAdapter

from task_cli.utils.types import Task, TaskUpdate

task_list_adapter = TypeAdapter(list[Task])


class DataService:
    def __init__(self):
        self.data_path = Path.cwd() / "data.json"
        if not self.data_path.exists():
            self.data_path.write_text(json.dumps([]))

    def read_tasks(self) -> list[Task]:
        return task_list_adapter.validate_json(
            self.data_path.read_text(encoding="utf-8")
        )

    def write_tasks(self, tasks: list[Task]) -> None:
        json_bytes = task_list_adapter.dump_json(tasks, indent=2)
        self.data_path.write_bytes(json_bytes)

    def update_task(self, id: int, **kwargs: Unpack[TaskUpdate]) -> None:
        tasks = self.read_tasks()

        for i, task in enumerate(tasks):
            if task.id != id:
                continue

            updates = {}
            if (description := kwargs.get("description")) is not None:
                updates["description"] = description
            if (status := kwargs.get("status")) is not None:
                updates["status"] = status

            updates["updated_at"] = datetime.now(UTC)

            tasks[i] = task.model_copy(update=updates)
            self.write_tasks(tasks)
            return

        raise RuntimeError("Task not found. Please provide correct ID.")
