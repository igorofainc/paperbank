"""
Tests for the registration app, 
They test if the registration proces is correctly functional
"""
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

# Create your tests here.

class RegistrationTestCase(TestCase):
    """
    Testing the registration app
    """
    def setUp(self):
        """
        Initializing
        """
        self.client = Client()

    def test_register(self):
        """
        Testing the main view of the app
        """
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
