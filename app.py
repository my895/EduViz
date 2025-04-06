from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
from collections import OrderedDict

app = Flask(__name__)
app.secret_key = 'techxerxer'

def load_timetable():
    with open('data/timetable.json', 'r') as file:
        timetable = json.load(file, object_pairs_hook=OrderedDict)
        return timetable

classroom_capacities = {
    "FFL 1": 60,
    "GFL 4": 50,
    "GFL 5": 55,
    "FFL 5": 45,
    "FFL 6": 30,
}

@app.route('/', methods=['GET', 'POST'])
def index():
    timetable = load_timetable()
    time_slots = list(OrderedDict.fromkeys(slot for schedule in timetable.values() for slot in schedule.keys()))
    
    if request.method == 'POST':
        selected_time_slot = request.form.get('time_slot')
        available_classrooms = check_availability(timetable, selected_time_slot)
        return render_template('result.html', available_classrooms=available_classrooms, time_slot=selected_time_slot)
    
    return render_template('index.html', time_slots=time_slots)

def check_availability(timetable, time_slot):
    available_classrooms = []
    for room, schedule in timetable.items():
        if time_slot in schedule and "Free" in schedule[time_slot]:
            available_classrooms.append({
                'classroom': room,
                'capacity': classroom_capacities.get(room, 'Unknown')
            })
    return available_classrooms

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            session['logged_in'] = True
            return redirect(url_for('admin'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    timetable = load_timetable()
    
    if request.method == 'POST':
        classroom = request.form.get('classroom')
        time_slot = request.form.get('time_slot')
        subjects = request.form.get('subjects').split(',')
        
        if classroom in timetable and time_slot:
            timetable[classroom][time_slot] = subjects
        
        with open('data/timetable.json', 'w') as file:
            json.dump(timetable, file, indent=4)
        return redirect(url_for('admin'))
    
    return render_template('admin.html', timetable=timetable, capacities=classroom_capacities)

@app.route('/remove_slot', methods=['POST'])
def remove_slot():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    classroom = request.form.get('classroom')
    time_slot = request.form.get('time_slot')

    timetable = load_timetable()
    if classroom in timetable and time_slot:
        timetable[classroom][time_slot] = ["Free"]

    with open('data/timetable.json', 'w') as file:
        json.dump(timetable, file, indent=4)

    return redirect(url_for('admin'))

@app.route('/api/timetable', methods=['GET'])
def api_timetable():
    timetable = load_timetable()
    return jsonify(timetable)

if __name__ == '__main__':
    app.run(debug=True)
