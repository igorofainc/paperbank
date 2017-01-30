from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your tests here.

class UsersTestCase(TestCase):
    """
    Testing the users
    """
    fixtures = ['allauth_test']

    def setUp(self):
        self.user = User.objects.create_user(
                             username="test_user",
                             email="test@paperbank.net",
                             password="test.test.test",
                         )

        self.client = Client()

    def test_logout(self):
        """
        Testing the view that logouts a user
        """
        #loggin in a user
        self.client.login(username="test_user", password="test.test.test")
        self.assertIn('_auth_user_id', self.client.session)

        #logging out
        response = self.client.get(reverse('sign_out'))
        self.assertRedirects(response, reverse('main_page'))
        self.assertNotIn('_auth_user_id', self.client.session)
