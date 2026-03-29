import streamlit as st
from models import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

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

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

# Create owner and pet
owner = Owner(owner_name)
pet = Pet(pet_name, species)
owner.add_pet(pet)

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    task = Task(task_title, int(duration), priority, pet)
    st.session_state.tasks.append(task)

if st.session_state.tasks:
    st.write("Current tasks:")
    task_data = [
        {"Title": t.title, "Duration (min)": t.duration_minutes, "Priority": t.priority, "Pet": t.pet.name if t.pet else "N/A"}
        for t in st.session_state.tasks
    ]
    st.table(task_data)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    if not st.session_state.tasks:
        st.error("No tasks to schedule.")
    else:
        scheduler = Scheduler()
        for task in st.session_state.tasks:
            scheduler.add_task(task)
        schedule = scheduler.generate_schedule()
        
        if schedule:
            st.success("Schedule generated!")
            for item in schedule:
                task = item['task']
                start = item['start_time']
                end = item['end_time']
                start_hour = start // 60
                start_min = start % 60
                end_hour = end // 60
                end_min = end % 60
                st.write(f"{start_hour:02d}:{start_min:02d} - {end_hour:02d}:{end_min:02d}: {task.title} for {task.pet.name if task.pet else 'Unknown'}")
        else:
            st.warning("No schedule could be generated (tasks may not fit in the day).")
