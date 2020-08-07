from ics import Calendar
import requests
import json
import arrow


def getEvents():
    f = open("IELET100120v.ics", "r")
    c = Calendar(f.read())

    events = []

    for event in c.events:
        event.begin = event.begin.replace(tzinfo='Europe/Oslo')
        event.end = event.end.replace(tzinfo='Europe/Oslo')
        eventObj = {
            'summary': event.name,
            'location': event.location,
            'description': event.description,
            'start': {
                'dateTime': event.begin.format('YYYY-MM-DDTHH:MM:SSZZ')
            }
        }
        print("\n")
        print(eventObj)
        

getEvents()
