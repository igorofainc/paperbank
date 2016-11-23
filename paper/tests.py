from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse


# Paper imports
from paper.models import Paper, Tag
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

        self.paper = Paper.objects.create(name="test_paper", paper_file=self.test_file)
        self.test_tag_one = self.paper.tags.create(name='test')
        self.test_tag_two = self.paper.tags.create(name='another_one')
        

        self.another_paper = Paper.objects.create(name='another_paper.pdf',  paper_file=self.test_file)
        self.another_paper.tags.add(self.test_tag_one)
        
        print self.paper
        print self.test_tag_one

    def test_models(self):
        """
        Testing the creation of papers
        """
        self.assertEqual(Paper.objects.all().count(), 2)


    def test_landing_page(self):
        """
        Testing the rendering of the landing page
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

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


    def test_tag_filter(self):
        """
        Testing the filtering of papers with 
        tags 
        """
        # Testing with an invalid tag, response should be a redirect to the main page
        response = self.client.get(reverse('filter_by_tag', args=['none']))
        self.assertEqual(response.status_code, 302)

        # Testing with a valid tag
        response = self.client.get(reverse('filter_by_tag', args=[self.test_tag_one.name]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['papers_page'].object_list), 2)


    def test_utils(self):
        """
        Testing the paper utils
        """
        # Testing the get_page function checking if no exceptions thrown
        papers = Paper.objects.all()
        get_page(papers, 1) # Running with a valid integer
        get_page(papers, 25) # Running with an empty page
        get_page(papers, 's') # Running with an invalid page

        # Test get main page context dict
        context_dict = get_main_page_context_dict() 
        self.assertEqual(context_dict['number_of_papers'], 2)
 

