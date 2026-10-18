from copy import deepcopy

from data import INITIAL_TASKS, Filter, Task

_tasks: list[Task] = deepcopy(INITIAL_TASKS)


def filter_tasks(all_tasks: list[Task], status: Filter) -> list[Task]:
    # TODO: implement filtering for "all" | "active" | "completed"
    return all_tasks


def get_tasks(status: str = "all") -> list[Task]:
    normalized = status if status in {"all", "active", "completed"} else "all"
    return filter_tasks(_tasks, normalized)  # type: ignore[arg-type]


def toggle_task(task_id: int) -> Task | None:
    for task in _tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            return deepcopy(task)
    return None
