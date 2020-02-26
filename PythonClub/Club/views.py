from .models import Meeting, Resource, MeetingMinutes, Event
from django.shortcuts import render, get_object_or_404
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def loginmessage(request):
    return render(request, 'club/loginmessage.html')


def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')


def index(request):
    return render(request, 'club/index.html')


def gettypes(request):
    resource_list = Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list': resource_list})


def getmeetings(request):
    meetings_list = Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meetings_list': meetings_list})


def meetingdetails(request, id):
    meet = get_object_or_404(Meeting, pk=id)
    meet = Meeting.objects.get(pk=id)
    # discount=prod.memberdiscount
    # reviews=Review.objects.filter(product=id).count()
    context = {
        'meet': meet,
        # 'discount' : discount,
        # 'reviews' : reviews,
    }
    return render(request, 'club/meetingdetails.html', context=context)


@login_required
def newMeeting(request):
    form = MeetingForm
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = MeetingForm()
    else:
        form = MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})


@login_required
def newResource(request):
    form = ResourceForm
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = ResourceForm()
    else:
        form = ResourceForm()
    return render(request, 'club/newresource.html', {'form': form})
