from ics import Calendar
import requests
import json
import arrow

def getEvents(url):
    c = Calendar(icsCalendar.read())

    events = []
    for event in c.events:
        #event.begin = event.begin.replace(tzinfo='Europe/Oslo')
        #event.end = event.end.replace(tzinfo='Europe/Oslo')
        eventObj = {
            'summary': str(event.name),
            'location': str(event.location),
            'description': str(event.description),
            'start': {
                'dateTime': str(event.begin),
                'timeZone': "Europe/Oslo"
            },
            'end': {
                'dateTime': str(event.end),
                'timeZone': "Europe/Oslo"
            },
        }
        events.append(eventObj)
    return events
