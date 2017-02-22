from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse

from paper.models import Paper

# Create your tests here.

class ApiTestCase(TestCase):
    """
    Tests for the api class
    """
    def setUp(self):
 
        # Creating the paper instance
        self.test_file = SimpleUploadedFile(name='test_file.pdf',
                                            content='testing file', content_type='application/pdf')

        self.paper = Paper.objects.create(name="test_paper", paper_file=self.test_file)
        
        # Client instance
        self.client = Client()

    def test_get_papers(self):
        response = self.client.get(reverse('get_papers_api'))  
         
        # Test if the validity of the response
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertDictEqual(data[0], {'id': 1, 'name': 'test_paper'})
