from pawpal_system import Task, Pet, Owner, Scheduler

# Create owner
owner = Owner("Kali")

# Create pets
dog = Pet("Buddy", "Dog")
cat = Pet("Luna", "Cat")

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create tasks
task1 = Task("Feed Buddy", "08:00", "Daily")
task2 = Task("Walk Buddy", "10:00", "Daily")
task3 = Task("Feed Luna", "09:00", "Daily")
task4 = Task("Bath Buddy", "08:00", "Daily")  # Duplicate time for conflict test

# Add tasks to pets
dog.add_task(task1)
dog.add_task(task2)
dog.add_task(task4)
cat.add_task(task3)

# Create scheduler
scheduler = Scheduler(owner)

# Get all tasks
tasks = scheduler.get_all_tasks()

# Sort tasks
sorted_tasks = scheduler.sort_by_time(tasks)

# Print schedule
print("Today's Schedule:\n")

for task in sorted_tasks:
    status = "Done" if task.completed else "Not Done"
    print(f"{task.time} - {task.description} ({status})")

conflicts = scheduler.detect_conflicts(sorted_tasks)
if conflicts:
    print("\nConflicts:")
    for c in conflicts:
        print(c)