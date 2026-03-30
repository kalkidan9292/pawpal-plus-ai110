import pytest
from pawpal_system import Task, Pet


class TestTask:
    def test_mark_complete_changes_status(self):
        """Verify that calling mark_complete() actually changes the task's status."""
        # Arrange
        task = Task(description="Feed the cat", time="08:00", frequency="daily")

        # Assert initial state
        assert task.completed is False

        # Act
        task.mark_complete()

        # Assert final state
        assert task.completed is True


class TestPet:
    def test_add_task_increases_task_count(self):
        """Verify that adding a task to a Pet increases that pet's task count."""
        # Arrange
        pet_type: str = "cat"
        pet = Pet(name="Whiskers", pet_type=pet_type)
        task = Task(description="Feed the cat", time="08:00", frequency="daily")

        # Assert initial state
        assert len(pet.tasks) == 0

        # Act
        pet.add_task(task)

        # Assert final state
        assert len(pet.tasks) == 1
        assert pet.tasks[0] == task


def test_sorting_tasks_by_time():
    from pawpal_system import Scheduler, Owner

    owner = Owner("Kali")
    scheduler = Scheduler(owner)

    t1 = Task("Task1", "10:00", "daily")
    t2 = Task("Task2", "08:00", "daily")
    t3 = Task("Task3", "09:00", "daily")

    tasks = [t1, t2, t3]
    sorted_tasks = scheduler.sort_by_time(tasks)

    assert sorted_tasks[0].time == "08:00"
    assert sorted_tasks[1].time == "09:00"
    assert sorted_tasks[2].time == "10:00"


def test_conflict_detection():
    from pawpal_system import Scheduler, Owner

    owner = Owner("Kali")
    scheduler = Scheduler(owner)

    t1 = Task("Feed", "08:00", "daily")
    t2 = Task("Walk", "08:00", "daily")

    tasks = [t1, t2]
    conflicts = scheduler.detect_conflicts(tasks)

    assert len(conflicts) == 1


def test_recurring_task_creation():
    task = Task("Feed", "08:00", "daily")

    new_task = task.mark_complete()

    assert task.completed is True
    assert new_task is not None
    assert new_task.description == "Feed"
