from dataclasses import dataclass, field
from typing import Any, Callable, Literal, Optional


TaskStatus = Literal[
    "PENDING",
    "RUNNING",
    "SUCCESS",
    "FAILED",
]


@dataclass(slots=True)
class Task:
    """
    Represents a single unit of work in the workflow.
    """

    name: str

    func: Callable[..., Any]

    retries: int = 0

    status: TaskStatus = "PENDING"

    execution_time: float = 0.0

    error: Optional[Exception] = None

    metadata: dict[str, Any] = field(default_factory=dict)

    def reset(self) -> None:
        """
        Reset the task to its initial state.
        """
        self.status = "PENDING"
        self.execution_time = 0.0
        self.error = None