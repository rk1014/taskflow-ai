def get_planning_prompt(user_input):
    """
    Generate a prompt for the AI to create a structured daily plan
    
    Args:
        user_input (str): User's natural language input
        
    Returns:
        str: Formatted prompt for the AI
    """
    prompt = f"""
You are a productivity assistant. From the following unstructured task list, extract and organize the tasks into clear categories. Add realistic time estimates and propose a daily schedule order.

User Input: "{user_input}"

Please create a structured daily plan with the following format:

{{
    "categories": {{
        "🎯 Priority Tasks": [
            {{"task": "task description", "time_estimate": "time estimate"}}
        ],
        "📨 Communication": [
            {{"task": "task description", "time_estimate": "time estimate"}}
        ],
        "🛒 Personal": [
            {{"task": "task description", "time_estimate": "time estimate"}}
        ],
        "💼 Work": [
            {{"task": "task description", "time_estimate": "time estimate"}}
        ]
    }},
    "suggested_schedule": [
        {{"time": "9:00 AM", "task": "description"}},
        {{"time": "11:00 AM", "task": "description"}}
    ],
    "total_estimated_time": "total time"
}}

Guidelines:
1. Categorize tasks by priority and type
2. Add realistic time estimates (15 min, 30 min, 1 hr, 2 hrs, etc.)
3. Suggest a logical order for the day
4. Focus on the most important tasks first
5. Include breaks and buffer time
6. Total time should be reasonable for a workday (6-8 hours)

Return only the JSON structure, no additional text.
"""
    return prompt.strip() 