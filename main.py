#!/bin/python3

import json
import turtle
import urllib.request

#using the international space station API:
url = 'http://api.open-notify.org/astros.json'

#calling the web service to retrieve data:
response = urllib.request.urlopen(url)

#loading JSON response into a Python data structure:
result = json.loads(response.read())

#this will print the value associated with the key 'number' in the result directory
numberOfPeople = result['number']

print('There are', numberOfPeople, 'people on the ISS:')

#the value associated with the 'people' key is a list of dictionaries
people = result['people']

#the 'name' and 'craft' key will extract the information we want from the entries in people
for p in people:
	print(p['name'])

#####Getting the Location of the ISS#####
