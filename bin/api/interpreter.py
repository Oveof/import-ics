from ics import Calendar
import requests
import json
import arrow


def getEvents(icsCalendar = open('IELET100120v.ics')):
    c = Calendar(icsCalendar.read())

    events = []

    for event in c.events:
        event.begin = event.begin.replace(tzinfo='Europe/Oslo')
        event.end = event.end.replace(tzinfo='Europe/Oslo')
        eventObj = {
            'summary': event.name,
            'location': event.location,
            'description': event.description,
            'start': {
                'dateTime': event.begin.format('YYYY-MM-DDTHH:MM:SSZZ'),
                'timezone': "Europe/Oslo"
            },
            'end': {
                'datetime': event.end.format('YYYY-MM-DDTHH:MM:SSZZ'),
                'timezone': "Europe/Oslo"
            },
        }
        events.append(json.dumps(eventObj))
    return events
        
getEvents()