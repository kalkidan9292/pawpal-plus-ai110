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
