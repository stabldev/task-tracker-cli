from datetime import datetime
from typing import Literal, TypedDict

type TaskStatus = Literal["todo", "in-progress", "done"]


class Task(TypedDict):
    id: int
    description: str
    status: TaskStatus
    created_at: datetime
    updated_at: datetime


class TaskUpdate(TypedDict, total=False):
    description: str
    status: TaskStatus
