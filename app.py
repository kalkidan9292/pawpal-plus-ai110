import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

# STEP 2: Fix the "memory reset" problem
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Kali")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

# STEP 3: Add a Pet (connect UI → your code)
st.header("Add a Pet")

pet_name = st.text_input("Pet Name", key="pet_name")
pet_type = st.text_input("Pet Type", key="pet_type")

if st.button("Add Pet") and pet_name and pet_type:
    new_pet = Pet(pet_name, pet_type)
    st.session_state.owner.add_pet(new_pet)
    st.success(f"{pet_name} added!")
    # Clear inputs
    st.session_state.pet_name = ""
    st.session_state.pet_type = ""
    st.rerun()

# STEP 4: Add a Task (this is the real connection)
st.header("Add a Task")

task_desc = st.text_input("Task Description", key="task_desc")
task_time = st.text_input("Time (HH:MM)", key="task_time")
task_freq = st.text_input("Frequency", key="task_freq")

# choose pet
pet_names = [pet.name for pet in st.session_state.owner.pets]
if pet_names:
    selected_pet_name = st.selectbox("Select Pet", pet_names)

    if st.button("Add Task") and task_desc and task_time and task_freq:
        task = Task(task_desc, task_time, task_freq)

        # find correct pet
        for pet in st.session_state.owner.pets:
            if pet.name == selected_pet_name:
                pet.add_task(task)

        st.success("Task added!")
        # Clear inputs
        st.session_state.task_desc = ""
        st.session_state.task_time = ""
        st.session_state.task_freq = ""
        st.rerun()
else:
    st.info("Please add a pet first before creating tasks.")

# STEP 5: Display Schedule (prove your logic works in UI)
st.header("Today's Schedule")

if st.session_state.owner.pets:
    scheduler = Scheduler(st.session_state.owner)
    tasks = scheduler.get_all_tasks()
    sorted_tasks = scheduler.sort_by_time(tasks)

    if sorted_tasks:
        for task in sorted_tasks:
            # Find which pet owns this task
            pet_name = "Unknown"
            for pet in st.session_state.owner.pets:
                if task in pet.tasks:
                    pet_name = pet.name
                    break

            emoji = "🟢"
            if task.priority == "High":
                emoji = "🔴"
            elif task.priority == "Medium":
                emoji = "🟡"

            st.write(f"{emoji} {task.time} - {task.description} ({pet_name}) - {task.priority}")

        conflicts = scheduler.detect_conflicts(sorted_tasks)
        if conflicts:
            st.warning("⚠️ Scheduling Conflict Detected!")
            for c in conflicts:
                st.write(c)
    else:
        st.info("No tasks scheduled yet.")
else:
    st.info("Add some pets and tasks to see your schedule!")
