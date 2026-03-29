class Owner:
    def __init__(self, name, preferences=None):
        self.name = name
        self.preferences = preferences or {}
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)
        pet.owner = self

    def view_pets(self):
        return self.pets


class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.tasks = []
        self.owner = None

    def add_task(self, task):
        self.tasks.append(task)
        task.pet = self

    def get_tasks(self):
        return self.tasks


class Task:
    def __init__(self, title, duration_minutes, priority, pet=None):
        self.title = title
        self.duration_minutes = duration_minutes
        self.priority = priority
        self.pet = pet

    def update_task(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def display_task(self):
        return f"Task: {self.title}, Duration: {self.duration_minutes} min, Priority: {self.priority}"


class Scheduler:
    def __init__(self, available_time=None):
        self.tasks = []
        self.available_time = available_time or {'start': 480, 'end': 1320}  # 8 AM to 10 PM in minutes

    def generate_schedule(self):
        sorted_tasks = self.sort_tasks_by_priority()
        schedule = []
        current_time = self.available_time['start']
        for task in sorted_tasks:
            if current_time + task.duration_minutes <= self.available_time['end']:
                schedule.append({
                    'task': task,
                    'start_time': current_time,
                    'end_time': current_time + task.duration_minutes
                })
                current_time += task.duration_minutes
            else:
                # For now, skip tasks that don't fit
                pass
        return schedule

    def sort_tasks_by_priority(self):
        priority_order = {'high': 0, 'medium': 1, 'low': 2}
        return sorted(self.tasks, key=lambda t: priority_order.get(t.priority, 3))

    def resolve_conflicts(self):
        # Basic conflict resolution: just return sorted tasks
        # Could be enhanced to handle overlaps
        return self.sort_tasks_by_priority()