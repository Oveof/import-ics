
def deleteAll():
    oldEvents = service.events().list(calendarId=CALENDAR_ID, singleEvents=True).execute()
    for oldEvent in oldEvents['items']:
        service.events().delete(calendarId=CALENDAR_ID, eventId=oldEvent['id']).execute()