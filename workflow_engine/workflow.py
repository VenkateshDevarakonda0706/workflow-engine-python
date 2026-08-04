from collections.abc import Generator
from .task import Task

class Workflow:
    """
    Represents a collection of tasks
    """
    def __init__(self) -> None:
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        """
        Add a task to workflow
        """
        self.tasks.append(task)

    def __iter__(self) -> Generator[Task, None, None]:
        """
        Iterate over wrokflow task.
        """
        yield from self.tasks

    def reset(self) -> None:
        """
        Reset all tasks.
        """
        for task in self.tasks:
            task.reset()

    def __len__(self) -> int:
        return len(self.tasks)