from ics import Calendar
import requests
import json
import arrow


def getEvents(icsCalendar):
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
                'timezone': event.begin.tzinfo
            },
            'end': {
                'datetime': event.end.format('YYYY-MM-DDTHH:MM:SSZZ'),
                'timezone': event.end.tzinfo
            }
        }
        print("\n")
        print(eventObj)
        
