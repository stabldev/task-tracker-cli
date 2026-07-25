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

    def _write(self, data: str) -> None:
        with open(self.data_path, "w", encoding="utf-8") as file:
            file.write(data)

    def _read(self) -> str:
        with open(self.data_path) as file:
            data = file.read()
            return data

    def read_tasks(self) -> list[Task]:
        return [Task(**item) for item in json.loads(self._read())]

    def write_tasks(self, tasks: Iterable[Task]) -> None:
        tasks_str = json.dumps(tasks, default=str, indent=2)
        self._write(tasks_str)
