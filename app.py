from flask import Flask, render_template, request, jsonify
from api.scheduler import TaskScheduler
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

# Initialize the task scheduler
scheduler = TaskScheduler()

@app.route('/')
def index():
    """Main page for TaskFlow AI"""
    return render_template('index.html')

@app.route('/api/plan', methods=['POST'])
def create_plan():
    """API endpoint to create a daily plan from natural language input"""
    try:
        data = request.get_json()
        user_input = data.get('input', '')
        
        if not user_input:
            return jsonify({'error': 'No input provided'}), 400
        
        # Generate the structured plan
        plan = scheduler.create_daily_plan(user_input)
        
        return jsonify({
            'success': True,
            'plan': plan
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/save-plan', methods=['POST'])
def save_plan():
    """Save a plan to local storage (simulated)"""
    try:
        data = request.get_json()
        plan_data = data.get('plan', {})
        date = data.get('date', '')
        
        # In a real app, you'd save to database
        # For now, we'll just return success
        return jsonify({
            'success': True,
            'message': 'Plan saved successfully'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/load-plan', methods=['GET'])
def load_plan():
    """Load a saved plan (simulated)"""
    try:
        date = request.args.get('date', '')
        
        # In a real app, you'd load from database
        # For now, return empty plan
        return jsonify({
            'success': True,
            'plan': {}
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 