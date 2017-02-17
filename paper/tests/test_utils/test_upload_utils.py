from django.test import TestCase

from paper.utils.paper_upload_utils import get_tags_from_string


class PaperUploadUtilsTestCase(TestCase):
    """
    Testing the utils that help in uploading a papper
    """
    
    def test_get_tags_from_string(self):
        """
        Testing the function that returns tag instances
        from a tag string
        """
        tag_string = 'maths, mid-term'
        tags = get_tags_from_string(tag_string)
        tags_name_list = [tags[0].name, tags[1].name]
        self.assertListEqual(tags_name_list, ['maths', 'mid-term'])
