from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.gettypes, name='resources'),
    path('getmeetings/', views.getmeetings, name='meetings'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('newResource/', views.newResource, name='newresource'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
