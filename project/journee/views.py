from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from journee.models import Traveler, PointOfInterest, Event
from datetime import datetime

import google.oauth2.credentials
import google_auth_oauthlib.flow
import os

import urllib, json

# flow = google_auth_oauthlib.flow.Flow.from_client_config(
#     client_config = {"web":{"client_id":"680374767023-7v1uabqifrqh3ok9p8vktq4ef62k3js2.apps.googleusercontent.com","project_id":"brownbears18-193419","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://accounts.google.com/o/oauth2/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"myZAS5-6DRxSF0vbKnAHyRG8","redirect_uris":["http://127.0.0.1:8000/oauth2callback"],"javascript_origins":["http://127.0.0.1:8000"]}},
#     scopes=[])
# 
# flow.redirect_uri = 'http://127.0.0.1:8000/oauth2callback'
# 
# authorization_url, state = flow.authorization_url(
#     access_type='offline',
#     include_granted_scopes='true')

    
SCOPES = ['https://www.googleapis.com/auth/userinfo.email']

# Create your views here.
def index(request):
	return render(request, "journee/index.html")

def login(request):
    return render(request, "journee/login.html")
    
def myinfo(request):
    return HttpResponse(request.session.get('user'))

def get_google_data(request):
    url = request.GET.get('url')
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    destinations = data.get("destination_addresses")
    rows = data.get("rows")
    distances = []
    for i in range(len(rows)):
        distances.append((i, rows[i]['elements'][0]['distance']['text']))
    distances.sort(key=lambda x: x[1])
    final_list = []
    for i in range(len(destinations)):
        final_list.append(destinations[distances[i][0]])
    # print(final_list)
    return render(request, "journee/map.html")


def trips(request):
    return HttpResponse('yay!')
    
def auth(request):
    # r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    # return HttpResponse(request.GET.get('session_state'))
    email = request.META.get('USER')
    try:
        user = Traveler.objects.get(email=email)
    except ObjectDoesNotExist:
        Traveler.objects.create(email=email)
    request.session['user'] = email
    return redirect('myinfo')
    
def logout(request):
    request.session['user'] = None
    return HttpResponse('logged out')
    
def calendar(request):
    # return render(request, "journee/calendar.html")
    events = []
    for event in Event.objects.all():
        event = {'title': event.place_id, 'placeId': event.place_id, 
            'proposedBy': event.proposed_by.email, 
            'startsAt': event.start_datetime.strftime("%a %d %b %Y %H:%M:%S"), 
            'endsAt': event.end_datetime.strftime("%a %d %b %Y %H:%M:%S")}
        events.append(event)
    return render(request, 'journee/calendar.html', context={'events': events})
    
    
def add_event(request):
    # if request.method == 'GET':
    #     return HttpResponse('Does not support get request')
    # elif request.method == 'POST':
    #     # TODO: check if POI exists alrdy
    #     Event.objects.create(start_datetime=request.GET.get('start'), end_datetime=request.GET.get('end'), proposed_by=Traveler.objects.get(email=request.session.get('user')))
    # return render(request, "journee/calendar.html")
    
    # start = datetime.strptime(request.GET.get('start'), '%Y-%m-%d %H:%M')
    # end = datetime.strptime(request.GET.get('end'), '%Y-%m-%d %H:%M')
    start_datetime = request.GET.get('start_datetime')
    end_datetime = request.GET.get('end_datetime')
    if request.method == 'GET':
        Event.objects.create(start_datetime=start_datetime, end_datetime=end_datetime, 
            proposed_by=Traveler.objects.get(email=request.session.get('user')), place=PointOfInterest.objects.get(place_id=request.GET.get('place_id')))
    return render(request, "journee/calendar.html")

def delete_event(request):
    start_datetime = request.GET.get('start_datetime')
    end_datetime = request.GET.get('end_datetime')
    if request.method == 'GET':
        event = Event.objects.filter(start_datetime=start_datetime, end_datetime=end_datetime, 
            place=PointOfInterest.objects.get(place_id=request.GET.get('place_id')))[0]
        event.delete()
    return render(request, "journee/calendar.html")

def map(request):
    return render(request, "journee/map.html")