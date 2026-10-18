from typing import Literal, TypedDict


Priority = Literal["low", "medium", "high"]
Filter = Literal["all", "active", "completed"]


class Task(TypedDict):
    id: int
    title: str
    completed: bool
    priority: Priority


INITIAL_TASKS: list[Task] = [
    {"id": 1, "title": "Review candidate applications", "completed": False, "priority": "high"},
    {"id": 2, "title": "Update project documentation", "completed": True, "priority": "medium"},
    {"id": 3, "title": "Prepare weekly report", "completed": False, "priority": "low"},
    {"id": 4, "title": "Fix authentication bug", "completed": False, "priority": "high"},
    {"id": 5, "title": "Schedule team retrospective", "completed": True, "priority": "low"},
    {"id": 6, "title": "Refactor dashboard layout", "completed": False, "priority": "medium"},
    {"id": 7, "title": "Write unit tests for utils", "completed": False, "priority": "medium"},
]
