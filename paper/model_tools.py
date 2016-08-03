"""
This file contains helper functions for 
the paper models
"""


def uploaded_paper_name(paper, filename):
    """
    Formats the uploaded file to 
    a new name 
    """
    initial = 'uploads/'
    name = paper.name + '-paperbank' + '.pdf'

    return initial + name

