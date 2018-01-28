from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('get_google_data', views.get_google_data, name='get_google_data'),
    path('logout', views.logout, name='logout'),
    path('myinfo', views.myinfo, name='myinfo'),
    path('add_event', views.add_event, name='add_event'),
    path('trips', views.trips, name='trips'),
    path('auth/complete/google-oauth2/', views.auth, name='auth'),
    path('calendar', views.calendar, name='calendar'),
    path('map', views.map, name='map'),
    path('auth/', include('social_django.urls', namespace='social')),
]
