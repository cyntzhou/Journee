from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('myinfo', views.myinfo, name='myinfo'),
    path('add_event', views.add_event, name='add_event'),
    path('trips', views.trips, name='trips'),
    path('auth/complete/google-oauth2/', views.auth, name='auth'),
    path('calendar', views.calendar, name='calendar'),
    
    path('auth/', include('social_django.urls', namespace='social')),
]