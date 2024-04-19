from django.test import TestCase, Client
from .models import Page

class PageViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.page = Page.objects.create(header='Test Header', body='Test Body', footer='Test Footer')

    def test_page_view_with_valid_id(self):
        response = self.client.get(f'/page/{self.page.id}/')
        self.assertEqual(response.status_code, 200)

    def test_page_view_with_invalid_id1(self):
        response = self.client.get('/page/12345/')
        self.assertEqual(response.status_code, 404)

    def test_page_view_with_invalid_id2(self):
        response = self.client.get('/page')
        self.assertEqual(response.status_code, 404)

    def test_page_view_with_invalid_id3(self):
        response = self.client.get('/page/xyz')
        self.assertEqual(response.status_code, 404)