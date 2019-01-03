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

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print("longtitude", lon, "\n", "latitude", lat, "\n")

#####Creating a Map to Display Location#####

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)
