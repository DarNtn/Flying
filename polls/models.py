from django.db import models
from mongoengine import *

connect('flying')
# Create your models here.
class Airports(Document):
	
	airportID = IntField()
	name = StringField(max_length=150)
	city = StringField(max_length=100)
	country = StringField(max_length=100)
	iata = StringField(max_length=10)
	icao = StringField(max_length=10)
	lat = IntField()
	lon = IntField()
	alt = IntField()
	timezone = IntField()
	dst = StringField(max_length=25)
	tz_db = StringField(max_length=100)
	type = StringField(max_length=100)
	source = StringField(max_length=50)

	meta = {
		'ordering': ['-name']
	}

	def __lt__(self, otro):
		return str(self.name) < str(otro.name)

	def __gt__(self, otro):
		return str(self.name) > str(otro.name)

	def __str__(self):
		return self.name +" - " + self.city
	
	
class Airlines(Document):
	
	airlineID = IntField()
	name = StringField(max_length=150)
	alias = StringField(max_length=50, default="")	
	iata = StringField(max_length=10)
	icao = StringField(max_length=10)
	callsign = StringField(max_length=25)
	country = StringField(max_length=100)
	active = StringField(max_length=2)

	def __lt__(self, otro):
		return self.name < otro.name

	def __gt__(self, otro):
		return self.name > otro.name
	
	def __str__(self):
		return self.name +" - " + self.country
	
		

class Routes(Document):
	airline = StringField(max_length=100)
	airlineID = IntField()
	sAirport = StringField(max_length=10)
	sAirportID = IntField()
	dAirport = StringField(max_length=10)
	dAirportID = IntField()
	codeshare = StringField(max_length=10, default="")	
	stops = IntField(default=0)
	equipment = StringField(max_length=25)
