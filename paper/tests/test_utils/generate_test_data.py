"""
Contains functions that help in the,
Generation of testing data
"""
import random
import string

from django.core.files.uploadedfile import SimpleUploadedFile

from reportlab.pdfgen import canvas

from paper.models import Paper, Tag


def generate_test_papers(number_of_papers):
    """
    Generates and adds a number of papers to the database.
    This should only be used in testing.
    
    @param number_of_papers - The number of papers to be generated
    """
    # Generating needed attributes for the papers
    tag = Tag.objects.create(name='test_tag' + ''.join(
                                                    random.choice(string.lowercase) for i in range(6)) )
                                                    #  ^ Avoiding integrityError: tag already exists

    test_paper_file = SimpleUploadedFile(name='test_paper.pdf',content='Test file', content_type='application/pdf')

    # Using reportlab to write content to pdf files
    c = canvas.Canvas(test_paper_file)
    c.drawString(100, 100, "Paperbank")
    c.save()


    for i in range(0, number_of_papers):
        paper = Paper.objects.create(name='S' + str(i) + ' Testing',
                             paper_file=test_paper_file)

        paper.tags.add(tag)
 
                              
