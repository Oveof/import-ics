from ics import Calendar
import requests
import json
import arrow


def getEvents(icsCalendar = open('IELET100120v.ics')):
    c = Calendar(icsCalendar.read())

    events = []
    i = 0

    for event in c.events:
        print(i)
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
        i = i + 1
    print("\n" + events[150])
    len(events)
    return events
        
getEvents()