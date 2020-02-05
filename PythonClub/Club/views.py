from .models import Meeting, Resource, MeetingMinutes,Event
from django.shortcuts import render,get_object_or_404

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def gettypes(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html' ,{'resource_list' : resource_list})

def getmeetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meetings_list': meetings_list})

def meetingdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    meet=Meeting.objects.get(pk=id)
    #discount=prod.memberdiscount
    #reviews=Review.objects.filter(product=id).count()
    context={
        'meet' : meet,
        #'discount' : discount,
        #'reviews' : reviews,
    }
    return render(request, 'club/meetingdetails.html', context=context)