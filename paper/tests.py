from django.test import TestCase, Client, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings

from pprint import PrettyPrinter

# Paper imports
from paper.models import Paper, Subject
from paper.utils import get_page, get_main_page_context_dict

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

        self.subject = Subject.objects.create(name='test_subject')

        self.paper = Paper.objects.create(name="test_paper", subject=self.subject, paper_file=self.test_file)

        self.another_paper = Paper.objects.create(name='another_paper.pdf', subject=self.subject, paper_file=self.test_file)
 
 
    def test_models(self):
        """
        Testing the creation of papers
        """
        self.assertEqual(Paper.objects.all().count(), 2)
	print Paper.objects.first()
	print Paper.objects.first().subject



    def test_main_page(self):
	"""
	Testing the main page for the paper app
        """
        response = self.client.get('/papers')
	self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['papers_page'].object_list), 2)

    def test_search(self):
        """ 
        Testing the searching of the papers
        """
        response = self.client.get('/search', {'q': 'another'})
        self.assertEqual(response.status_code, 200)
  
        page = response.context['papers_page']
        self.assertEqual(len(page.object_list), 1)



