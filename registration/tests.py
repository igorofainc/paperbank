"""
Tests for the registration app, 
They test if the registration proces is correctly functional
"""
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from .models import Registrant
from .forms import RegistrantForm
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

        data = {'name': 'Test Name',
                'email': 'test@paperbank.net', 
                'phone_number': '250788000000',
                'school': 'Test School',
                'description': 'sample description',
        }

        # Testing the form
        registrant = RegistrantForm(data)
        self.assertTrue(registrant.is_valid())

        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Registrant.objects.all().count(), 1)
        print Registrant.objects.first()
      
