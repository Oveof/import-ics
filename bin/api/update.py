from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from interpreter import getEvents

from ics import Calendar
import requests
import json
import arrow

SCOPES = ['https://www.googleapis.com/auth/calendar']
CALENDAR_ID = 'kfj5jbndhv4liav49blpj7hurs@group.calendar.google.com'

def main():

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    c = Calendar(open("IELET100120v.ics").read())

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
        service.events().insert(calendarId=CALENDAR_ID, body=eventObj).execute()

#HELLOW

if __name__ == '__main__':
    main()