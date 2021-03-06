from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, ResourceForm
from django.urls import reverse
from django.contrib.auth.models import User

# ------------------------- Meeting Model --------------------


class MeetingTest(TestCase):
    # set up one time sample data
    def setup(self):
        meeting = Meeting(meetingtitle='TestMeeting',
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
        self.assertEqual(meeting.location,
                         'Galvanize  111 S Jackson St · Seattle')

    def test_agenda(self):
        meeting = self.setup()
        self.assertEqual(meeting.agenda, 'This is an agenda')

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

# ------------------------- Meeting Mintues Model --------------------


class MeetingMinutesTest(TestCase):
    # set up one time sample data
    def setup(self):
        meeting = Meeting(meetingtitle='TestMeeting')
        mid = MeetingMinutes(meetingid=meeting,
                             # attendance='Bob',
                             minutes='This is the meeting mintues from last weeks meeting')
        return mid

    def test_string(self):
        mid = self.setup()
        self.assertEqual(str(mid), mid.meetingid)

    # def test_attendance(self):
        #mid = self.setup()
        #self.assertEqual(mid.attendance, 'Bob,Joe')

    def test_minutes(self):
        mid = self.setup()
        self.assertEqual(
            mid.minutes, 'This is the meeting mintues from last weeks meeting')

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminute')

# ------------------------- Resource Type Model --------------------


class ResourceTypeTest(TestCase):
    # set up one time sample data
    def setup(self):
        res = Resource(resourcetype="Education",
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

# ------------------------- Event Model --------------------


class EventTest(TestCase):
    # set up one time sample data
    def setup(self):
        ev = Event(eventtitle="Party",
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


# tests for views
# ------------------------- Index View --------------------
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

# ------------------------- Get Rsources View --------------------


class GetResourcesTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)

# ------------------------- Get Meetings View --------------------


class GetMeetingsTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        self.meeting = Meeting.objects.create(
            meetingtitle='test_meeting', meetingdate='2019-04-02', meetingtime='18:30:00', agenda="This is a test")

    def test_meeting_detail_success(self):
        response = self.client.get(
            reverse('meetingdetails', args=(self.meeting.id,)))
        # Assert that self.post is actually returned by the post_detail view
        self.assertEqual(response.status_code, 200)

    # Form tests

# ------------------------- Resource Form--------------------


class Resource_Form_Test(TestCase):
    def test_typeform_is_valid(self):
        form = ResourceForm(
            data={'resourcetype': "type1", 'description': "some type"})
        self.assertTrue(form.is_valid())

    def test_typeform_minus_descript(self):
        form = ResourceForm(data={'resourcetype': "type1"})
        self.assertFalse(form.is_valid())

    def test_typeform_empty(self):
        form = ResourceForm(data={'resourcetype': ""})
        self.assertFalse(form.is_valid())

# ------------------------- Meeting Form --------------------


class Meeting_Form_Test(TestCase):
    def test_meetingform_is_valid(self):
        form = MeetingForm(data={'meetingtitle': "Test Meeting", 'meetingdate': "2020-03-04",
                                 'meetingtime': "18:00:00", 'location': "Amazon", 'agenda': "This is a test agenda"})
        self.assertTrue(form.is_valid())

    def test_meetingform_minus_agenda(self):
        form = MeetingForm(data={'meetingtitle': "Test Meeting", 'meetingdate': "2020-03-04",
                                 'meetingtime': "18:00:00", 'location': "Amazon"})
        self.assertTrue(form.is_valid())

    def test_meetingform_empty(self):
        form = MeetingForm(data={'meetingtitle': ""})
        self.assertFalse(form.is_valid())

# ------------------------- New Rsource --------------------


class New_Resource_authentication_test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser1', password='P@ssw0rd1')
        self.type = Resource.objects.create(resourcetype='laptop')
        self.res = Resource.objects.create(resourcetype=self.type, user=self.test_user,
                                           dateentered='2019-04-02', url='http://www.dell.com', description="a product")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newresource'))
        self.assertRedirects(
            response, '/accounts/login/?next=/club/newResource/')

    def test_Logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='P@ssw0rd1')
        response = self.client.get(reverse('newresource'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/newresource.html')

# ------------------------- New Meeting --------------------


class New_Meeting_authentication_test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser1', password='P@ssw0rd1')
        self.meet = Meeting.objects.create(meetingtitle='Test Meeting', meetingdate='2020-03-04', meetingtime='18:00:00', location='Amazon',
                                           agenda='This is a test agenda')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newmeeting'))
        self.assertRedirects(
            response, '/accounts/login/?next=/club/newMeeting/')

    def test_Logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='P@ssw0rd1')
        response = self.client.get(reverse('newmeeting'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/newmeeting.html')
