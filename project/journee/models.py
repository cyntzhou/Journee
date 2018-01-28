from django.db import models

# Create your models here.

import datetime
from datetime import date

class Traveler(models.Model):
	first_name = models.CharField(max_length=50, null=True)
	last_name = models.CharField(max_length=50, null=True)
	facebook_username = models.CharField(max_length=50, null=True)

class PointOfInterest(models.Model):
	place_id = models.CharField(max_length=50)

class Event(models.Model):
	date_event = models.DateField
	hour = models.CharField(max_length=4)
	place_id = models.CharField(max_length=50)

class TravelGroup(models.Model):
	members = models.ManyToManyField(Traveler)
	trip_name = models.CharField(max_length=50)
	interested_points = models.ManyToManyField(PointOfInterest)
	iternary = models.ManyToManyField(Event)



