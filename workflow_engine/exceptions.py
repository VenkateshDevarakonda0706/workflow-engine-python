class WorkflowError(Exception):
    """
    Base exception for the workflow engine.
    """


class TaskExecutionError(WorkflowError):
    """
    Raised when a task execution fails.
    """


class WorkflowExecutionError(WorkflowError):
    """
    Raised when workflow execution fails.
    """


class RetryLimitExceededError(WorkflowError):
    """
    Raised when maximum retry attempts are exceeded.
    """