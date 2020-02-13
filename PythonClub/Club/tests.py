from django.test import TestCase
from .models import Meeting,MeetingMinutes,Resource,Event
from django.urls import reverse
from django.contrib.auth.models import User

class MeetingTest(TestCase):
   #set up one time sample data
   def setup(self):
       meeting=Meeting(meetingtitle='TestMeeting',
       meetingdate='2020-05-18',
       meetingtime='18:30:00',
       location='Galvanize  111 S Jackson St · Seattle',
       agenda='This is an agenda')
       return meeting

   def test_string(self):
       meeting = self.setup()
       self.assertEqual(str(meeting), meeting.meetingtitle)
    
   def test_date(self):
       meeting = self.setup()
       self.assertEqual(meeting.meetingdate, '2020-05-18')

   def test_time(self):
       meeting = self.setup()
       self.assertEqual(meeting.meetingtime, '18:30:00')

   def test_location(self):
       meeting = self.setup()
       self.assertEqual(meeting.location, 'Galvanize  111 S Jackson St · Seattle')

   def test_agenda(self):
       meeting = self.setup()
       self.assertEqual(meeting.agenda, 'This is an agenda')

   def test_table(self):
       self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
   #set up one time sample data
   def setup(self):
       mid=MeetingMinutes(meetingid='2',
       attendance='Bob,Joe',
       minutes='This is the meeting mintues from last weeks meeting')
       return mid

   def test_string(self):
       mid = self.setup()
       self.assertEqual(str(mid), mid.meetingid)

   def test_attendance(self):
       mid = self.setup()
       self.assertEqual(mid.attendance, 'Bob,Joe')
       
   def test_minutes(self):
       mid = self.setup()
       self.assertEqual(mid.minutes, 'This is the meeting mintues from last weeks meeting')

   def test_table(self):
       self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminute')

class ResourceTypeTest(TestCase):
   #set up one time sample data
   def setup(self):
       res=Resource(resourcetype="Education",
       url="https://www.pluralsight.com/paths/python",
       dateentered="2020-05-18",
       description="Pluralsight")
       return res

   def test_string(self):
       res = self.setup()
       self.assertEqual(str(res), res.resourcename)

   def test_resourcetype(self):
       res = self.setup()
       self.assertEqual(res.resourcetype, 'Education')

   def test_resourceurl(self):
       res = self.setup()
       self.assertEqual(res.url, 'https://www.pluralsight.com/paths/python')

   def test_resourcedateentered(self):
       res = self.setup()
       self.assertEqual(res.dateentered, '2020-05-18')

   def test_resourcedescription(self):
       res = self.setup()
       self.assertEqual(res.description, 'Pluralsight')

   def test_table(self):
       self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
       #set up one time sample data
   def setup(self):
       ev=Event(eventtitle="Party",
       location="Seattle",
       date="2020-05-18",
       time="18:30:00",
       description="This is the event")
       return ev

   def test_string(self):
       ev = self.setup()
       self.assertEqual(str(ev), ev.eventtitle)

   def test_eventlocation(self):
       res = self.setup()
       self.assertEqual(res.location, 'Seattle')

   def test_eventdate(self):
       res = self.setup()
       self.assertEqual(res.date, '2020-05-18')

   def test_eventtime(self):
       res = self.setup()
       self.assertEqual(res.time, '18:30:00')

   def test_eventdescription(self):
       res = self.setup()
       self.assertEqual(res.description, 'This is the event')

   def test_table(self):
       self.assertEqual(str(Event._meta.db_table), 'event')


#tests for views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetResourcesTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('resources'))
       self.assertEqual(response.status_code, 200)

class GetMeetingsTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('meetings'))
       self.assertEqual(response.status_code, 200)

   def setUp(self):
        self.meeting = Meeting.objects.create(meetingtitle='test_meeting',meetingdate='2019-04-02',meetingtime='18:30:00', agenda="This is a test")

   def test_meeting_detail_success(self):
        response = self.client.get(reverse('meetingdetails', args=(self.meeting.id,)))
        # Assert that self.post is actually returned by the post_detail view
        self.assertEqual(response.status_code, 200)