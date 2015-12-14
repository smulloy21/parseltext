from django.test import TestCase
from django.http import HttpRequest
from blogs.views import home_page

# Create your tests here.
class HomePageViewTest(TestCase):

    def test_home_page_returns_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>ParselText</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))
