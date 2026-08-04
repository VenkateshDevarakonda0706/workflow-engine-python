from workflow_engine.task import Task
from workflow_engine.workflow import Workflow


def hello():
    print("Hello World")


workflow = Workflow()

task = Task(
    name="Greeting",
    func=hello,
)

workflow.add_task(task)

print(f"Number of tasks: {len(workflow)}")

for task in workflow:
    print(task.name)