from django.test import TestCase, RequestFactory

from reviews.views import index


class TestIndexView(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()

    def test_index_view(self):
        request = self.factory.get('/')
        request.session = {}
        response = index(request)
        self.assertEquals(response.status_code, 200)
