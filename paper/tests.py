from django.test import TestCase, Client, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings


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
  
    def test_models(self):
        """
        Testing the upload of models
        """
        self.assertEqual(Paper.objects.all().count(), 1)


    @override_settings(DEBUG=True)
    def test_download(self):
        """
        Testing the download of the papers
        
        Note: This test is only testing the download of the papers on a development machine where
              debug is set to true
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

  
        response = self.client.post(self.paper.paper_file.url, {})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
