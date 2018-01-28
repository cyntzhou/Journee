from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from journee.models import Traveler

import google.oauth2.credentials
import google_auth_oauthlib.flow
import os
    
SCOPES = ['https://www.googleapis.com/auth/userinfo.email']

# Create your views here.
def index(request):
	return render(request, "journee/index.html")

def login(request):
    return render(request, "journee/login.html")
    
def myinfo(request):
    return HttpResponse(request.session.get('user'))

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
    return render(request, "journee/calendar.html")