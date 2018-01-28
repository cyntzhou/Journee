from django.contrib import admin
from .models import Traveler, PointOfInterest, Event, Trip

# Register your models here.

admin.site.register(Traveler)
admin.site.register(PointOfInterest)
admin.site.register(Event)
admin.site.register(Trip)