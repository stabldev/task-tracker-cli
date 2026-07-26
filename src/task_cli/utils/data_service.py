import json
from collections.abc import Iterable
from pathlib import Path

from task_cli.utils.types import Task


class DataService:
    def __init__(self):
        base_path = Path(__file__).resolve().parent.parent.parent.parent
        self.data_path = base_path / "data.json"
        if not self.data_path.exists():
            self.data_path.write_text(json.dumps([]))

    def read_tasks(self) -> list[Task]:
        with open(self.data_path) as file:
            data = file.read()

        return [Task(**item) for item in json.loads(data)]

    def write_tasks(self, tasks: Iterable[Task]) -> None:
        tasks_str = json.dumps(tasks, default=str, indent=2)
        with open(self.data_path, "w", encoding="utf-8") as file:
            file.write(tasks_str)
