from django.test import TestCase, Client, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings

from pprint import PrettyPrinter

# Create your tests here.
from paper.models import Paper

class PaperTest(TestCase):
    """
    Test Cases for the paper
    app
    """
    def setUp(self):
        """
        Setting up the database
        """
        self.client = Client()

        self.test_file = SimpleUploadedFile(name='test_file.pdf',
                                            content='testing file', content_type='application/pdf')

        self.paper = Paper.objects.create(name="test_paper", paper_file=self.test_file)

        self.another_paper = Paper.objects.create(name='another_paper.pdf', paper_file=self.test_file)
 
 
    def test_models(self):
        """
        Testing the upload of models
        """
        self.assertEqual(Paper.objects.all().count(), 2)


    def test_search(self):
        """ 
        Testing the searching of the papers
        """
        response = self.client.get('/search', {'q': 'another'})
        self.assertEqual(response.status_code, 200)
  
        page = response.context['papers_page']
        self.assertEqual(len(page.object_list), 1)


