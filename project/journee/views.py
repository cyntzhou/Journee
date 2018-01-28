from django.shortcuts import render, redirect
from django.http import HttpResponse

import google.oauth2.credentials
import google_auth_oauthlib.flow
import os
    
SCOPES = []

# Create your views here.
def index(request):
	return render(request, "journee/index.html")

def login(request):
    return render(request, "journee/login.html")

def trips(request):
    return HttpResponse('yay!')
    
def auth(request):
    return HttpResponse(request.GET.get('authuser'))
    
def calendar(request):
    return render(request, "journee/calendar.html")