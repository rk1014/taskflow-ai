# TaskFlow AI - Intelligent Daily Planner

 **Transform your thoughts into structured daily plans with AI-powered task organization**

TaskFlow AI is a smart productivity tool that converts natural language descriptions into organized, prioritized daily plans with time estimates and suggested schedules.

## ✨ Features

- **🤖 AI-Powered Planning**: Uses OpenAI GPT to intelligently categorize and organize tasks
- **📝 Natural Language Input**: Simply describe your day in plain English
- **🎯 Smart Categorization**: Automatically sorts tasks by priority and type
- **⏰ Time Estimates**: Realistic time estimates for each task
- **📅 Suggested Schedule**: AI-generated optimal daily schedule
- **🎨 Modern UI**: Beautiful, responsive design with Tailwind CSS
- **🎤 Voice Input**: Speech-to-text functionality for hands-free planning
- **🌙 Dark Mode**: Toggle between light and dark themes
- **💾 Save & Export**: Save plans and export as text files
- **⌨️ Keyboard Shortcuts**: Ctrl+Enter to generate plans quickly

##  Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key (optional, falls back to mock data)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd taskflow-ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 📖 Usage

### Basic Usage

1. **Describe your day** in the text area:
   ```
   "I need to finish the UI for the dashboard, follow up with the client, 
   prepare slides for tomorrow, and maybe finally go grocery shopping."
   ```

2. **Click "Generate Plan"** or press `Ctrl+Enter`

3. **Review your structured plan**:
   - Tasks organized by priority and category
   - Time estimates for each task
   - Suggested daily schedule
   - Total estimated time

### Advanced Features

- **Voice Input**: Click the microphone button to speak your tasks
- **Save Plans**: Click "Save Plan" to store your plan (simulated)
- **Export Plans**: Download your plan as a text file
- **Dark Mode**: Toggle the theme with the moon/sun button
- **Keyboard Shortcuts**: Use `Ctrl+Enter` to generate plans

##  Architecture

```
taskflow-ai/
├── app.py                 # Flask application
├── api/
│   ├── scheduler.py       # AI planning logic
│   └── prompt_templates.py # AI prompts
├── templates/
│   └── index.html        # Main UI template
├── static/
│   └── js/
│       └── app.js        # Frontend JavaScript
├── requirements.txt       # Python dependencies
└── README.md            # This file
```

## 🤖 AI Integration

### OpenAI API (Recommended)
- Set your `OPENAI_API_KEY` in the `.env` file
- Uses GPT-3.5-turbo for intelligent task analysis
- Provides the best categorization and time estimates

### Fallback Mode
- Works without API key using keyword-based categorization
- Provides basic task organization and mock data
- Perfect for testing and development

##  UI Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern Interface**: Clean, intuitive design with Tailwind CSS
- **Smooth Animations**: Hover effects and transitions
- **Real-time Feedback**: Loading states and notifications
- **Accessibility**: Keyboard navigation and screen reader support

##  Configuration

### Environment Variables

Create a `.env` file with:

```env
OPENAI_API_KEY=your_openai_api_key_here
SECRET_KEY=your_secret_key_here
FLASK_ENV=development
```

### Customization

- **Categories**: Modify `api/scheduler.py` to add custom categories
- **Styling**: Edit `templates/index.html` for UI changes
- **Prompts**: Customize AI prompts in `api/prompt_templates.py`

##  Deployment

### Local Development
```bash
python app.py
```

### Production Deployment

#### Option 1: Render
1. Connect your GitHub repository
2. Set environment variables
3. Deploy automatically

#### Option 2: Heroku
```bash
heroku create taskflow-ai
git push heroku main
```

#### Option 3: Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

##  Testing

### Manual Testing
1. Start the application
2. Enter various task descriptions
3. Test voice input functionality
4. Verify export and save features

### Example Inputs

**Work Day:**
```
"I need to finish the quarterly report, call the marketing team, 
review the budget proposal, and schedule next week's meetings."
```

**Personal Day:**
```
"I want to go grocery shopping, clean the house, 
call my mom, and maybe finally start that book I bought."
```

**Mixed Day:**
```
"Finish the client presentation, pick up dry cleaning, 
follow up on emails, and maybe hit the gym after work."
```

##  Future Enhancements

- [ ] **Calendar Integration**: Sync with Google Calendar, Outlook
- [ ] **Mobile App**: React Native version
- [ ] **Browser Extension**: Chrome/Firefox extension
- [ ] **Team Planning**: Collaborative planning features
- [ ] **Analytics**: Track productivity and time usage
- [ ] **Notifications**: Reminder system with push notifications
- [ ] **Templates**: Pre-built plan templates
- [ ] **AI Learning**: Improve suggestions based on user patterns

##  Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Acknowledgments

- OpenAI for providing the GPT API
- Tailwind CSS for the beautiful styling
- Font Awesome for the icons
- Flask for the web framework

---

**Built with ❤️ and AI** - Transform your productivity with TaskFlow AI! 