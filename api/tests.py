from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse

from paper.models import Paper, Tag


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
        self.paper.tags.create(name='test_tag')
        
        # Client instance
        self.client = Client()

    def test_get_papers(self):
        """
        Testing the view that returns all the data for all papers.
        """
        response = self.client.get(reverse('get_papers_api'))  
         
        # Test if the validity of the response
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertDictEqual(data[0], {'id': self.paper.id,
                                      'name': self.paper.name,
                                      'paper_file':self.paper.paper_file.url})

    def test_paper_detail(self):
        """
        Testing the function that returns the details for a given paper.
        """
        response = self.client.get(reverse('paper_detail_api', args=[1]))

        data = response.json()
        self.assertDictEqual(data, {'id': self.paper.id,
                                    'name': self.paper.name,
                                    'paper_file': self.paper.paper_file.url})

    def test_search(self):
        """
        Testing the endpoint for searching for papers
        """

        # When search returns empty
        response = self.client.get(reverse('paper_search_api'), {'q': 'empty'})
        data = response.json()
        self.assertFalse(data)

        # When search returns content
        response = self.client.get(reverse('paper_search_api'), {'q': 'test_p'})
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertDictEqual(data[0], {'id': self.paper.id,
                                       'name': self.paper.name,
                                       'paper_file': self.paper.paper_file.url})

    def test_filter(self):
        """
        Testing the endpoint that is responsible for searching
        """

        # When the tag is invalid
        response = self.client.get(reverse('filter_by_tag_api'), {'tag': 'empty'})
        data = response.json()
        self.assertFalse(data)

        # When it is a valid tag
        response = self.client.get(reverse('filter_by_tag_api'), {'tag': 'test_tag'})
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertDictEqual(data[0], {'id': self.paper.id,
                                       'name': self.paper.name,
                                       'paper_file': self.paper.paper_file.url})


