#!/usr/bin/env python3
"""
Test script for TaskFlow AI
This script tests the core functionality without requiring external dependencies
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_scheduler():
    """Test the TaskScheduler class with mock data"""
    print("🧪 Testing TaskScheduler...")
    
    try:
        from api.scheduler import TaskScheduler
        
        # Create scheduler instance
        scheduler = TaskScheduler()
        print("✅ TaskScheduler initialized successfully")
        
        # Test with sample input
        test_input = "I need to finish the UI for the dashboard, follow up with the client, prepare slides for tomorrow, and maybe finally go grocery shopping."
        
        print(f"📝 Testing with input: {test_input[:50]}...")
        
        # Generate plan
        plan = scheduler.create_daily_plan(test_input)
        
        print("✅ Plan generated successfully!")
        print(f"📊 Plan structure: {list(plan.keys())}")
        
        if 'categories' in plan:
            print("📋 Categories found:")
            for category, tasks in plan['categories'].items():
                print(f"  - {category}: {len(tasks)} tasks")
        
        if 'suggested_schedule' in plan:
            print(f"⏰ Schedule items: {len(plan['suggested_schedule'])}")
        
        if 'total_estimated_time' in plan:
            print(f"⏱️ Total time: {plan['total_estimated_time']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing scheduler: {e}")
        return False

def test_prompt_templates():
    """Test the prompt templates"""
    print("\n🧪 Testing prompt templates...")
    
    try:
        from api.prompt_templates import get_planning_prompt
        
        test_input = "Test input for prompt generation"
        prompt = get_planning_prompt(test_input)
        
        print("✅ Prompt template generated successfully")
        print(f"📝 Prompt length: {len(prompt)} characters")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing prompt templates: {e}")
        return False

def test_file_structure():
    """Test that all required files exist"""
    print("\n🧪 Testing file structure...")
    
    required_files = [
        'app.py',
        'api/__init__.py',
        'api/scheduler.py',
        'api/prompt_templates.py',
        'templates/index.html',
        'static/js/app.js',
        'requirements.txt',
        'README.md'
    ]
    
    missing_files = []
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MISSING")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n⚠️ Missing files: {missing_files}")
        return False
    else:
        print("\n✅ All required files present")
        return True

def main():
    """Run all tests"""
    print("🚀 TaskFlow AI - Application Test Suite")
    print("=" * 50)
    
    tests = [
        test_file_structure,
        test_prompt_templates,
        test_scheduler
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! TaskFlow AI is ready to use.")
        print("\n💡 To run the application:")
        print("   1. Install dependencies: pip install -r requirements.txt")
        print("   2. Set up environment variables (optional)")
        print("   3. Run: python app.py")
        print("   4. Open: http://localhost:5000")
    else:
        print("⚠️ Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 