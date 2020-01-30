from .models import Meeting, Resource, MeetingMinutes,Event
from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def gettypes(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html' ,{'resource_list' : resource_list})

