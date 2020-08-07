from ics import Calendar
import requests

f = open("IELET100120v.ics", "r")

c = Calendar(f.read())

