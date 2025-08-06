# TaskFlow AI

TaskFlow AI is an intelligent daily planner that turns natural language into a structured to-do list. It helps users organize their tasks with the following features:

- **Priorities:** Assign priority levels to tasks to focus on what matters most.
- **Time Estimates:** Get time estimates for tasks to plan your day efficiently.
- **Reminders:** Set reminders for important tasks to ensure nothing is overlooked.
- **Suggested Time Blocks:** Receive suggestions for optimal time blocks to complete tasks based on your schedule.

## Example Input
> "I need to finish the UI for the dashboard, follow up with the client, prepare slides for tomorrow, and maybe finally go grocery shopping."

## Example Output
```
🎯 Priority Tasks:
  - Finish UI for dashboard (2 hrs)
  - Prepare slides for presentation (1.5 hrs)

📨 Communication:
  - Follow up with client (15 min)

🛒 Personal:
  - Grocery shopping (45 min)

🕒 Suggested Order:
  9:00 AM - UI Work
  11:30 AM - Slide Prep
  1:00 PM - Client Follow-up
  2:00 PM - Grocery Run
```

## File Structure

```
/taskflow-ai/
├── app.py                 # Flask or FastAPI backend
├── /templates/            # HTML templates (if web)
│   └── index.html
├── /static/               # CSS, JS
├── /api/
│   ├── scheduler.py       # AI planning logic
│   └── prompt_templates.py
├── .env
├── requirements.txt
```

## Tech Stack

- Python (Flask or FastAPI)
- OpenAI API (or Hugging Face LLM)
- Optional: SQLite to save plans
- Tailwind CSS or Bootstrap for styling
- Deploy to: Hugging Face Spaces, Render, or Vercel

## Prompt Design

```python
"You are a productivity assistant. From the following unstructured task list, extract and organize the tasks into clear categories. Add realistic time estimates and propose a daily schedule order."
```

## Bonus Features

- Save/load plans per day
- LocalStorage or file export
- Theme toggle (light/dark)
- Keyboard shortcuts
- Add voice input (Web Speech API)

## Next Steps

- Turn into browser extension
- Add mobile support via React Native
- Offer “Pro” version with calendar sync and notifications
