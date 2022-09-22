from urllib import response
from django.test import TestCase

# Create your tests here.
class URLTests(TestCase):
    def test_testregistration(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        
        
# class URLTests(TestCase):
#     def test_testlogin(self):
#         response = self.client.get('/accounts/login/')
#         self.assertEqual(response.status_code, 200)
        
        
# class URLTests(TestCase):
#     def test_testlogout(self):
#         response = self.client.get('/accounts/logout/')
#         self.assertEqual(response.status_code, 200)
        
        
# class URLTests(TestCase):
#     def test_testdasboard(self):
#         response = self.client.get('/accounts/dashboard/')
#         self.assertEqual(response.status_code, 200)


# class URLTests(TestCase):
#     def test_testhistory(self):
#         response = self.client.get('/accounts/history/')
#         self.assertEqual(response.status_code, 200)
        
        
        
        
        