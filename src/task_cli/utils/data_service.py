import json
from pathlib import Path


class DataService:
    def __init__(self):
        base_path = Path(__file__).resolve().parent.parent.parent.parent
        self.data_path = base_path / "data.json"
        if not self.data_path.exists():
            self.data_path.write_text(json.dumps([]))

    def write(self, data: str) -> None:
        with open(self.data_path, "w", encoding="utf-8") as file:
            file.write(data)

    def read(self) -> str:
        with open(self.data_path) as file:
            data = file.read()
            return data
