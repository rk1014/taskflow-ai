// TaskFlow AI - Frontend JavaScript
class TaskFlowApp {
    constructor() {
        this.currentPlan = null;
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.setupVoiceInput();
        this.setupThemeToggle();
        this.updateCharCount();
    }

    setupEventListeners() {
        // Input handling
        const taskInput = document.getElementById('task-input');
        taskInput.addEventListener('input', () => this.updateCharCount());

        // Generate plan button
        document.getElementById('generate-plan').addEventListener('click', () => {
            this.generatePlan();
        });

        // Clear input button
        document.getElementById('clear-input').addEventListener('click', () => {
            this.clearInput();
        });

        // Save plan button
        document.getElementById('save-plan').addEventListener('click', () => {
            this.savePlan();
        });

        // Export plan button
        document.getElementById('export-plan').addEventListener('click', () => {
            this.exportPlan();
        });

        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 'Enter') {
                e.preventDefault();
                this.generatePlan();
            }
        });
    }

    setupVoiceInput() {
        const voiceButton = document.getElementById('voice-input');
        let isRecording = false;
        let recognition = null;

        // Check if speech recognition is available
        if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
            recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = 'en-US';

            recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript;
                document.getElementById('task-input').value = transcript;
                this.updateCharCount();
            };

            recognition.onerror = (event) => {
                console.error('Speech recognition error:', event.error);
                this.showNotification('Voice input error. Please try again.', 'error');
            };

            voiceButton.addEventListener('click', () => {
                if (!isRecording) {
                    recognition.start();
                    isRecording = true;
                    voiceButton.innerHTML = '<i class="fas fa-stop"></i>';
                    voiceButton.classList.add('bg-red-500');
                } else {
                    recognition.stop();
                    isRecording = false;
                    voiceButton.innerHTML = '<i class="fas fa-microphone"></i>';
                    voiceButton.classList.remove('bg-red-500');
                }
            });
        } else {
            voiceButton.style.display = 'none';
        }
    }

    setupThemeToggle() {
        const themeToggle = document.getElementById('theme-toggle');
        const isDark = localStorage.getItem('theme') === 'dark';
        
        if (isDark) {
            document.documentElement.classList.add('dark');
            themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
        }

        themeToggle.addEventListener('click', () => {
            const isDark = document.documentElement.classList.toggle('dark');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
            themeToggle.innerHTML = isDark ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
        });
    }

    updateCharCount() {
        const input = document.getElementById('task-input');
        const charCount = document.getElementById('char-count');
        charCount.textContent = input.value.length;
    }

    async generatePlan() {
        const input = document.getElementById('task-input');
        const userInput = input.value.trim();

        if (!userInput) {
            this.showNotification('Please describe your day first!', 'error');
            return;
        }

        // Show loading state
        this.showLoading(true);
        this.hideResults();

        try {
            const response = await fetch('/api/plan', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ input: userInput })
            });

            const data = await response.json();

            if (data.success) {
                this.currentPlan = data.plan;
                this.displayPlan(data.plan);
                this.showNotification('Plan generated successfully!', 'success');
            } else {
                throw new Error(data.error || 'Failed to generate plan');
            }
        } catch (error) {
            console.error('Error generating plan:', error);
            this.showNotification('Failed to generate plan. Please try again.', 'error');
        } finally {
            this.showLoading(false);
        }
    }

    displayPlan(plan) {
        this.displayCategories(plan.categories);
        this.displaySchedule(plan.suggested_schedule);
        this.updateTotalTime(plan.total_estimated_time);
        this.showResults();
    }

    displayCategories(categories) {
        const categoriesSection = document.getElementById('categories-section');
        categoriesSection.innerHTML = '';

        Object.entries(categories).forEach(([categoryName, tasks]) => {
            if (tasks.length === 0) return;

            const categoryCard = document.createElement('div');
            categoryCard.className = 'bg-white rounded-lg shadow-lg p-6 task-card';
            
            const emoji = this.getCategoryEmoji(categoryName);
            const color = this.getCategoryColor(categoryName);

            categoryCard.innerHTML = `
                <div class="flex items-center mb-4">
                    <span class="text-2xl mr-3">${emoji}</span>
                    <h3 class="text-lg font-semibold text-gray-800">${categoryName.replace(/^[^\s]*\s/, '')}</h3>
                </div>
                <div class="space-y-3">
                    ${tasks.map(task => `
                        <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                            <span class="text-gray-700">${task.task}</span>
                            <span class="text-sm font-medium text-${color}-600 bg-${color}-100 px-2 py-1 rounded">
                                ${task.time_estimate}
                            </span>
                        </div>
                    `).join('')}
                </div>
            `;

            categoriesSection.appendChild(categoryCard);
        });
    }

    displaySchedule(schedule) {
        const scheduleList = document.getElementById('schedule-list');
        scheduleList.innerHTML = '';

        schedule.forEach((item, index) => {
            const scheduleItem = document.createElement('div');
            scheduleItem.className = 'flex items-center p-4 bg-gray-50 rounded-lg';
            
            scheduleItem.innerHTML = `
                <div class="flex items-center space-x-4">
                    <div class="w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center text-sm font-semibold">
                        ${index + 1}
                    </div>
                    <div class="flex-1">
                        <div class="font-semibold text-gray-800">${item.time}</div>
                        <div class="text-gray-600">${item.task}</div>
                    </div>
                </div>
            `;

            scheduleList.appendChild(scheduleItem);
        });
    }

    updateTotalTime(totalTime) {
        document.getElementById('total-time').textContent = totalTime;
    }

    getCategoryEmoji(categoryName) {
        const emojiMap = {
            '🎯 Priority Tasks': '🎯',
            '📨 Communication': '📨',
            '🛒 Personal': '🛒',
            '💼 Work': '💼',
            '🏠 Home': '🏠',
            '📚 Learning': '📚'
        };
        return emojiMap[categoryName] || '📋';
    }

    getCategoryColor(categoryName) {
        const colorMap = {
            '🎯 Priority Tasks': 'red',
            '📨 Communication': 'blue',
            '🛒 Personal': 'green',
            '💼 Work': 'purple',
            '🏠 Home': 'yellow',
            '📚 Learning': 'indigo'
        };
        return colorMap[categoryName] || 'gray';
    }

    async savePlan() {
        if (!this.currentPlan) {
            this.showNotification('No plan to save!', 'error');
            return;
        }

        try {
            const response = await fetch('/api/save-plan', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    plan: this.currentPlan,
                    date: new Date().toISOString().split('T')[0]
                })
            });

            const data = await response.json();

            if (data.success) {
                this.showNotification('Plan saved successfully!', 'success');
            } else {
                throw new Error(data.error || 'Failed to save plan');
            }
        } catch (error) {
            console.error('Error saving plan:', error);
            this.showNotification('Failed to save plan. Please try again.', 'error');
        }
    }

    exportPlan() {
        if (!this.currentPlan) {
            this.showNotification('No plan to export!', 'error');
            return;
        }

        const planText = this.formatPlanForExport(this.currentPlan);
        const blob = new Blob([planText], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        
        const a = document.createElement('a');
        a.href = url;
        a.download = `taskflow-plan-${new Date().toISOString().split('T')[0]}.txt`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);

        this.showNotification('Plan exported successfully!', 'success');
    }

    formatPlanForExport(plan) {
        let text = 'TaskFlow AI - Daily Plan\n';
        text += '=' * 30 + '\n\n';

        // Categories
        Object.entries(plan.categories).forEach(([categoryName, tasks]) => {
            if (tasks.length === 0) return;
            
            text += `${categoryName}:\n`;
            tasks.forEach(task => {
                text += `  - ${task.task} (${task.time_estimate})\n`;
            });
            text += '\n';
        });

        // Schedule
        text += '🕒 Suggested Schedule:\n';
        plan.suggested_schedule.forEach(item => {
            text += `  ${item.time} - ${item.task}\n`;
        });

        text += `\nTotal Estimated Time: ${plan.total_estimated_time}\n`;
        text += `Generated on: ${new Date().toLocaleString()}\n`;

        return text;
    }

    clearInput() {
        document.getElementById('task-input').value = '';
        this.updateCharCount();
        this.hideResults();
    }

    showLoading(show) {
        const loading = document.getElementById('loading');
        loading.style.display = show ? 'block' : 'none';
    }

    showResults() {
        document.getElementById('plan-results').style.display = 'block';
    }

    hideResults() {
        document.getElementById('plan-results').style.display = 'none';
    }

    showNotification(message, type = 'info') {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `fixed top-4 right-4 p-4 rounded-lg shadow-lg z-50 transition-all duration-300 transform translate-x-full`;
        
        const colors = {
            success: 'bg-green-500 text-white',
            error: 'bg-red-500 text-white',
            info: 'bg-blue-500 text-white'
        };

        notification.className += ` ${colors[type]}`;
        notification.innerHTML = `
            <div class="flex items-center space-x-2">
                <i class="fas fa-${type === 'success' ? 'check' : type === 'error' ? 'exclamation-triangle' : 'info-circle'}"></i>
                <span>${message}</span>
            </div>
        `;

        document.body.appendChild(notification);

        // Animate in
        setTimeout(() => {
            notification.classList.remove('translate-x-full');
        }, 100);

        // Remove after 3 seconds
        setTimeout(() => {
            notification.classList.add('translate-x-full');
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 300);
        }, 3000);
    }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new TaskFlowApp();
}); 