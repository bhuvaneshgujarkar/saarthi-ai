import random
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

dashboard_students = [
    {'name': 'Ethan Harper', 'department': 'Computer Science', 'risk': 'High', 'activity': '2 days ago'},
    {'name': 'Olivia Bennett', 'department': 'Engineering', 'risk': 'Medium', 'activity': '1 week ago'},
    {'name': 'Noah Carter', 'department': 'Mathematics', 'risk': 'Low', 'activity': '3 days ago'},
    {'name': 'Ava Morgan', 'department': 'Physics', 'risk': 'High', 'activity': '1 day ago'},
    {'name': 'Liam Foster', 'department': 'Chemistry', 'risk': 'Medium', 'activity': '2 weeks ago'},
    {'name': 'Isabella Reed', 'department': 'Biology', 'risk': 'Low', 'activity': '4 days ago'},
]

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html', active_page='home')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', students=dashboard_students, active_page='dashboard')

@app.route('/predictions')
def predictions():
    point1 = random.randint(0, 100)
    point2 = random.randint(0, 100)

    cuts = sorted([0, point1, point2, 100])
    percentages = [cuts[1] - cuts[0], cuts[2] - cuts[1], cuts[3] - cuts[2]]
    
    random.shuffle(percentages)

    low_percentage = percentages[0]
    medium_percentage = percentages[1]
    high_percentage = percentages[2]

    return render_template(
        'predictions.html', 
        active_page='predictions',
        low_risk_percentage=low_percentage,
        medium_risk_percentage=medium_percentage,
        high_risk_percentage=high_percentage
    )

@app.route('/resources')
def resources():
    return render_template('resources.html', active_page='resources')

@app.route('/community')
def community():
    return render_template('community.html', active_page='community')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html', active_page='chatbot')

@app.route('/get_bot_response', methods=['POST'])
def get_bot_response():
    user_message = request.json.get('message').lower()
    bot_response = "I'm sorry, I don't quite understand. Could you ask in a different way?"
    
    if 'hello' in user_message or 'hi' in user_message:
        bot_response = "Hello there! How can I assist you today?"
    elif 'coursework' in user_message or 'overwhelmed' in user_message:
        bot_response = "Coursework can definitely be challenging. What specific subject is giving you the most trouble?"
    elif 'exam' in user_message or 'test' in user_message:
        bot_response = "Feeling nervous about an exam is normal. Have you tried breaking down your study material into smaller chunks?"
    elif 'thank you' in user_message or 'thanks' in user_message:
        bot_response = "You're welcome! Is there anything else I can help with?"
    
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)