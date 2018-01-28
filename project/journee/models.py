from django.db import models

# Create your models here.

import datetime
from datetime import date

class Traveler(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)

class PointOfInterest(models.Model):
    place_id = models.CharField(max_length=50)

class Event(models.Model):
    start_datetime = models.DateTimeField(default=date.today)
    end_datetime = models.DateTimeField(default=date.today)
    place = models.ForeignKey('PointOfInterest', on_delete=models.CASCADE, default=None)
    proposed_by = models.ForeignKey('Traveler', on_delete=models.CASCADE, default=None)

class Trip(models.Model):
    travelers = models.ManyToManyField(Traveler)
    name = models.CharField(max_length=50)
    interested_points = models.ManyToManyField(PointOfInterest)
    itinerary = models.ManyToManyField(Event)



