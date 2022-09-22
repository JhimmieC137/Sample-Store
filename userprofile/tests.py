from urllib import response
from django.test import TestCase

# Create your tests here.
class URLTests(TestCase):
    def test_testregistration(self):
        response = self.client.get('register/')
        self.assertEqual(response.status_code, 200)