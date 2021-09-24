from flask import render_template, request
from app import app
from models.event_list import events, add_new_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods = ['POST'])
def add_event():
    print(request.form)
    event_date = request.form["date"]
    event_name = request.form["name"]
    event_guests_num = request.form["guests_num"]
    event_room = request.form["room"]
    event_description = request.form["description"]
    new_event = Event(event_date, event_name, event_guests_num, event_room, event_description)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events = events)
    # or return redirect /events