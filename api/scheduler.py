import openai
import os
from datetime import datetime, timedelta
from api.prompt_templates import get_planning_prompt
import json

class TaskScheduler:
    def __init__(self):
        """Initialize the TaskScheduler with OpenAI API key"""
        self.api_key = os.getenv('OPENAI_API_KEY')
        if self.api_key:
            openai.api_key = self.api_key
        else:
            print("Warning: OPENAI_API_KEY not found in environment variables")
    
    def create_daily_plan(self, user_input):
        """
        Convert natural language input into a structured daily plan
        
        Args:
            user_input (str): Natural language description of tasks
            
        Returns:
            dict: Structured plan with categories, tasks, and schedule
        """
        try:
            if not self.api_key:
                # Fallback to mock data if no API key
                return self._create_mock_plan(user_input)
            
            # Create the prompt for the AI
            prompt = get_planning_prompt(user_input)
            
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a productivity assistant that creates structured daily plans."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            # Parse the AI response
            ai_response = response.choices[0].message.content
            return self._parse_ai_response(ai_response)
            
        except Exception as e:
            print(f"Error creating plan: {e}")
            return self._create_mock_plan(user_input)
    
    def _parse_ai_response(self, ai_response):
        """Parse the AI response into structured format"""
        try:
            # Try to extract JSON from the response
            if '{' in ai_response and '}' in ai_response:
                start = ai_response.find('{')
                end = ai_response.rfind('}') + 1
                json_str = ai_response[start:end]
                return json.loads(json_str)
            else:
                # Fallback to text parsing
                return self._parse_text_response(ai_response)
        except:
            return self._parse_text_response(ai_response)
    
    def _parse_text_response(self, text):
        """Parse text response into structured format"""
        # This is a simplified parser for text responses
        plan = {
            'categories': {},
            'suggested_schedule': [],
            'total_estimated_time': '0 hours'
        }
        
        lines = text.split('\n')
        current_category = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Detect category headers
            if any(emoji in line for emoji in ['🎯', '📨', '🛒', '💼', '🏠', '📚']):
                current_category = line.split(':', 1)[0].strip()
                plan['categories'][current_category] = []
            elif current_category and line.startswith('-'):
                # Extract task and time estimate
                task_text = line[1:].strip()
                plan['categories'][current_category].append({
                    'task': task_text,
                    'time_estimate': self._extract_time_estimate(task_text)
                })
        
        return plan
    
    def _extract_time_estimate(self, task_text):
        """Extract time estimate from task text"""
        import re
        time_pattern = r'\((\d+(?:\.\d+)?\s*(?:hr|hour|min|minute)s?)\)'
        match = re.search(time_pattern, task_text, re.IGNORECASE)
        if match:
            return match.group(1)
        return "30 min"  # Default estimate
    
    def _create_mock_plan(self, user_input):
        """Create a mock plan when API is not available"""
        # Simple keyword-based categorization
        input_lower = user_input.lower()
        
        plan = {
            'categories': {
                '🎯 Priority Tasks': [],
                '📨 Communication': [],
                '🛒 Personal': [],
                '💼 Work': []
            },
            'suggested_schedule': [
                {'time': '9:00 AM', 'task': 'Start with priority tasks'},
                {'time': '11:00 AM', 'task': 'Communication tasks'},
                {'time': '2:00 PM', 'task': 'Personal tasks'},
                {'time': '4:00 PM', 'task': 'Review and wrap up'}
            ],
            'total_estimated_time': '6 hours'
        }
        
        # Categorize based on keywords
        if any(word in input_lower for word in ['ui', 'dashboard', 'slides', 'presentation']):
            plan['categories']['🎯 Priority Tasks'].append({
                'task': 'Finish UI for dashboard',
                'time_estimate': '2 hrs'
            })
            plan['categories']['🎯 Priority Tasks'].append({
                'task': 'Prepare slides for presentation',
                'time_estimate': '1.5 hrs'
            })
        
        if any(word in input_lower for word in ['client', 'follow up', 'email', 'call']):
            plan['categories']['📨 Communication'].append({
                'task': 'Follow up with client',
                'time_estimate': '15 min'
            })
        
        if any(word in input_lower for word in ['grocery', 'shopping', 'store']):
            plan['categories']['🛒 Personal'].append({
                'task': 'Grocery shopping',
                'time_estimate': '45 min'
            })
        
        return plan 