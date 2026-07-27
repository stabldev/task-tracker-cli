from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Literal, TypedDict

type TaskStatus = Literal["todo", "in-progress", "done"]


@dataclass
class Task:
    id: int
    description: str
    status: TaskStatus
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(
            id=data["id"],
            description=data["description"],
            status=data["status"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def update(
        self, description: str | None = None, status: TaskStatus | None = None
    ) -> None:
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        self.updated_at = datetime.now(UTC)


class TaskUpdate(TypedDict, total=False):
    description: str
    status: TaskStatus
