# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

The user can add and manage pet information, such as the pet’s name and type.

The user can create and track daily care tasks, including things like feeding, walking, or giving medication, with details like duration and priority.

The user can generate a daily schedule that organizes tasks based on time and priority, helping them decide what to do and when.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

I reviewed my design with AI and identified a few potential improvements.

One issue was that tasks were being sorted using string values for time, which could lead to incorrect ordering. I improved this by using Python’s datetime parsing to ensure tasks are sorted correctly.

I also considered adding more advanced features like task IDs and additional filtering options, but decided to keep the design simple to maintain readability and focus on core functionality.

These decisions helped balance functionality with simplicity.


## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

My scheduler considers time and priority as the main constraints. Tasks are ordered based on priority level (High, Medium, Low) and then sorted by time.

I decided these constraints mattered most because pet care tasks often vary in urgency, and some tasks must be completed earlier in the day. Combining priority with time ensures that important tasks are handled first while still maintaining a logical schedule.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff in my scheduler is that conflict detection only checks for tasks with the exact same time rather than overlapping durations. This simplifies the logic and keeps the system easy to understand, but it may not catch more complex scheduling conflicts.

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI tools like GitHub Copilot throughout the project for brainstorming system design, generating class structures, and implementing methods such as sorting, filtering, and conflict detection.

The most helpful prompts were specific questions about how to structure relationships between classes and how to implement sorting using datetime. AI also helped speed up debugging by suggesting fixes for errors and improving code readability.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

One moment where I did not accept an AI suggestion as-is was when it recommended adding advanced features like task IDs and complex filtering logic. I chose to simplify the design because those features added unnecessary complexity for this project.

I evaluated the suggestions by considering whether they improved clarity and usability. If the solution made the system harder to understand or maintain, I modified or rejected it.

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested task completion, adding tasks to pets, sorting tasks by time, conflict detection, and recurring task behavior.

These tests were important to ensure that the core functionality of the system worked correctly and that tasks were being managed and displayed as expected.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

I am very confident that my scheduler works correctly for the main use cases, including sorting, filtering, and conflict detection.

If I had more time, I would test additional edge cases such as invalid time formats, overlapping task durations, and handling a larger number of tasks across multiple pets.

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with how the system integrates the backend logic with the Streamlit UI. The app is interactive and clearly demonstrates the scheduling features.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I had another iteration, I would improve the system by adding more advanced scheduling features such as overlapping time detection, better recurring task handling, and data persistence.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

AI tools like GitHub Copilot were very helpful during this project. I used Copilot to generate class structures, suggest methods, and help implement sorting and filtering logic.

The most effective feature was inline suggestions and chat assistance, which helped me quickly build and debug my scheduler logic.

One suggestion I modified was adding too much complexity, such as advanced filtering and task IDs. I chose to keep the system simple and readable instead.

Using separate chat sessions helped me stay organized by focusing on one phase at a time without mixing design, implementation, and testing.

I learned that even with powerful AI tools, I still needed to guide the design decisions and keep the system simple. Acting as the “lead architect” meant choosing clarity and functionality over unnecessary complexity.

## 6. Final Status

- Backend architecture completed: Task, Pet, Owner, Scheduler (dataclasses and methods implemented)
- UI integration completed: Streamlit connected to logic, session state persistence
- Smart scheduling implemented: sort by time, filter by status, detect conflict time overlap, recurring task support
- Testing completed: 5 pytest tests passed (task complete, add task, sorting, conflict detection, recurring)
- Documentation updated: README + reflection
- Git operations done: final commits and push to main

Final state: project is complete and ready to submit.  
Confidence level: very high.
