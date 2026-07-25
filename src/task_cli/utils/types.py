from datetime import datetime
from typing import Literal, TypedDict


class Task(TypedDict):
    id: int
    description: str
    status: Literal["todo", "in-progress", "done"]
    created_at: datetime
    updated_at: datetime
