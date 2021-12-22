from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from .models import Publisher
from . import views


class TestPublisherModel(TestCase):
    """Test the publisher's model"""

    def setUp(self) -> None:
        self.p = Publisher(name='Packt',
                           website="www.packt.com",
                           email='contact@packt.com')

    def test_create_publisher(self):
        self.assertIsInstance(self.p, Publisher)

    def test_str_representation(self):
        self.assertEquals(str(self.p), 'Packt')


class TestGreetingView(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_greeting_view(self):
        response = self.client.get('/test/greeting', follow=True)
        self.assertEquals(response.status_code, 200)


class TestLoggedInGreetingView(TestCase):
    def setUp(self) -> None:
        self.test_user = User.objects.create_user(username='testuser', password='testuserpassword@paktsite')
        self.test_user.save()
        self.client = Client()
        self.factory = RequestFactory()

    def test_user_greeting_not_authenicated(self):
        request = self.factory.get('/test/greeting_user/')
        request.user = AnonymousUser()
        response = views.greeting_view_user(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/test/greeting_user/')
        request.user = self.test_user
        response = views.greeting_view_user(request)
        self.assertEquals(response.status_code, 200)


# Create your tests here.
