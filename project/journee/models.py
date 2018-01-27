from django.db import models

# Create your models here.

import datetime
from datetime import date

class Traveler(models.Model):
	first_name = models.CharField
	last_name = models.CharField
	facebook_email = models.CharField



class travelGroup(models.Model):
	trip_name = models.Charfield