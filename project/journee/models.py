from django.db import models

# Create your models here.

import datetime
from datetime import date

class Traveler(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	facebook_username = models.CharField(max_length=50)

class TravelGroup(models.Model):
	members = models.ManyToMAnyField(Traveler)
	trip_name = models.Charfield(max_length-50)
	interested_points = models.ManyToManyField(PointOfInterest)
	iternary = models.ManyToManyField(Event)

class Event(models.Model):
	date_event = models.DateField
	hour = nodels.charfield(max_length=4)
	place_id = models.CharField(max_length=50)


class PointOfInterest(models.Model):
	place_id = models.CharField(max_length=50)
