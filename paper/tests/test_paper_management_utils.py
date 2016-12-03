"""
Test the paper management utils.
"""
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from paper.models import Paper, Tag
from paper.utils.paper_management_utils import get_storage_size, get_storage_size_bytes

class PaperManagementUtilsTestCase(TestCase):
    """
    Testing the paper management utils
    """
   
    def setUp(self):
        """
        Initializing 
        """
        self.paper_file = SimpleUploadedFile(name='test_file',
                                             content='Test',
                                             content_type='image/jpeg')
        
        self.tag = Tag.objects.create(name='test_tag')
 
        self.paper = Paper.objects.create(name='test_paper', paper_file=self.paper_file)


    def test_get_storage_size(self):
        """
        Testing the get storage size util
        """
        # Just executing to see if there is no exceptions in the code
        size = get_storage_size(size='mb')
        size = get_storage_size(size='kb')
        size = get_storage_size(size='gb')
         
        # invalidsize just in case
        # self.assertRaises(get_storage_size(size='invalid'), Exception)

    def test_get_storage_size_bytes(self):
        """
        Testing the get storage size, util
        """
        size = get_storage_size_bytes()
        self.assertEqual(size, 4)

        #Testing filter by tags
        self.paper.tags.add(self.tag)
        size = get_storage_size_bytes(self.tag)     
        self.assertEqual(size, 4)                                    
