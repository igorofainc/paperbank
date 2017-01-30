from django.test import TestCase

from paper.forms import PaperForm


class PaperFormTestCase(TestCase):
    """
    Testing the paper forms.
    """
    def setUp(self):
        print "Initializing"

    def test_paper_form(self):
        """
        Testing the paper form
        """
        form = PaperForm 
        # other tests for the form should be here, add them when you add new functionality
