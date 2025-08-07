#!/usr/bin/env python3
"""
TaskFlow AI - Demo Script
This script demonstrates the core functionality of TaskFlow AI
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def demo_task_planning():
    """Demonstrate task planning functionality"""
    print("🎯 TaskFlow AI - Intelligent Daily Planner")
    print("=" * 50)
    
    # Sample inputs
    sample_inputs = [
        "I need to finish the UI for the dashboard, follow up with the client, prepare slides for tomorrow, and maybe finally go grocery shopping.",
        "Today I want to clean the house, call my mom, go to the gym, and maybe start reading that book I bought last week.",
        "I have a busy day: finish quarterly report, call marketing team, review budget, and schedule next week's meetings."
    ]
    
    try:
        from api.scheduler import TaskScheduler
        
        scheduler = TaskScheduler()
        print("✅ TaskScheduler initialized successfully")
        
        for i, input_text in enumerate(sample_inputs, 1):
            print(f"\n📝 Example {i}:")
            print(f"Input: {input_text}")
            
            # Generate plan
            plan = scheduler.create_daily_plan(input_text)
            
            print("📊 Generated Plan:")
            
            # Display categories
            if 'categories' in plan:
                for category, tasks in plan['categories'].items():
                    if tasks:  # Only show categories with tasks
                        print(f"\n{category}:")
                        for task in tasks:
                            print(f"  - {task['task']} ({task['time_estimate']})")
            
            # Display schedule
            if 'suggested_schedule' in plan and plan['suggested_schedule']:
                print(f"\n🕒 Suggested Schedule:")
                for item in plan['suggested_schedule']:
                    print(f"  {item['time']} - {item['task']}")
            
            # Display total time
            if 'total_estimated_time' in plan:
                print(f"\n⏱️ Total Estimated Time: {plan['total_estimated_time']}")
            
            print("-" * 50)
        
        print("\n🎉 Demo completed successfully!")
        print("\n💡 Key Features Demonstrated:")
        print("  ✅ Natural language input processing")
        print("  ✅ Intelligent task categorization")
        print("  ✅ Time estimation")
        print("  ✅ Schedule generation")
        print("  ✅ Fallback mode (works without API key)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during demo: {e}")
        import traceback
        traceback.print_exc()
        return False

def show_usage_instructions():
    """Show how to use the application"""
    print("\n🚀 How to Use TaskFlow AI:")
    print("=" * 40)
    print("1. Install dependencies:")
    print("   pip install -r requirements.txt")
    print("\n2. Set up environment (optional):")
    print("   Create .env file with OPENAI_API_KEY")
    print("\n3. Run the application:")
    print("   python app.py")
    print("\n4. Open your browser:")
    print("   http://localhost:5000")
    print("\n5. Start planning your day!")
    print("   - Type or speak your tasks")
    print("   - Click 'Generate Plan'")
    print("   - Review your organized schedule")
    print("   - Save or export your plan")

if __name__ == "__main__":
    success = demo_task_planning()
    if success:
        show_usage_instructions()
    else:
        print("\n⚠️ Demo failed. Please check the error messages above.")
        sys.exit(1) 