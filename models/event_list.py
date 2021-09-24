from models.event import *

event1 = Event("23/09/21", "Fringe", 50, "Underbelly", "comedy show", True)
event2 = Event("24/09/21", "Tattoo", 1000, "Edinburgh Castle", "marching band", False)

events = [event1, event2]

def add_new_event(event):
    events.append(event)