from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class Task:
    description: str
    time: str
    frequency: str
    completed: bool = False

    def mark_complete(self) -> Optional['Task']:
        """Mark the task as completed and return a new recurring task if applicable."""
        self.completed = True

        if self.frequency.lower() == "daily":
            # For daily tasks, keep the same time
            return Task(self.description, self.time, self.frequency)
        elif self.frequency.lower() == "weekly":
            # For weekly tasks, keep the same time (simplified)
            return Task(self.description, self.time, self.frequency)

        return None


@dataclass
class Pet:
    name: str
    pet_type: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to the pet's task list."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's pet list."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks from all pets owned by this owner."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    def __init__(self, owner: Owner) -> None:
        """Initialize the scheduler with an owner."""
        self.owner = owner

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks from the owner's pets."""
        return self.owner.get_all_tasks()

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks by their scheduled time."""
        return sorted(tasks, key=lambda task: datetime.strptime(task.time, "%H:%M"))

    def filter_tasks(self, tasks: List[Task], completed: Optional[bool] = None, pet_name: Optional[str] = None) -> List[Task]:
        """Filter tasks by completion status and/or pet name."""
        filtered = tasks

        if completed is not None:
            filtered = [t for t in filtered if t.completed == completed]

        if pet_name:
            filtered = [
                t for t in filtered
                if any(t in pet.tasks and pet.name == pet_name for pet in self.owner.pets)
            ]

        return filtered

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """Detect conflicts for tasks scheduled at the same time."""
        conflicts = []
        seen_times = {}

        for task in tasks:
            if task.time in seen_times:
                conflicts.append(f"Conflict at {task.time}: {task.description} overlaps with {seen_times[task.time]}")
            else:
                seen_times[task.time] = task.description

        return conflicts