from django.shortcuts import render, redirect
from django.http import HttpResponse

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
    
SCOPES = []

# Create your views here.
def index(request):
	return render(request, "journee/index.html")

def login(request):
    return render(request, "journee/login.html")

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
    print(final_list)
    return render(request, "journee/map.html")


def trips(request):
    return HttpResponse('yay!')
    
def auth(request):
    return HttpResponse(request.GET.get('authuser'))
    
def calendar(request):
    return render(request, "journee/calendar.html")

def map(request):
    return render(request, "journee/map.html")
