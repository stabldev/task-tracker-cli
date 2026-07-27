from datetime import UTC, datetime
from typing import Literal, TypedDict

from pydantic import BaseModel, Field

type TaskStatus = Literal["todo", "in-progress", "done"]


class Task(BaseModel):
    id: int
    description: str
    status: TaskStatus
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class TaskUpdate(TypedDict, total=False):
    description: str
    status: TaskStatus
