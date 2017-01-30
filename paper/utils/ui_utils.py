"""
Main utils for the paper app
"""
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from paper.models import Paper
from paper.forms import PaperForm


def get_main_page_context_dict():
    """
    Returns values that are rendered on the
    main application page.
    """
    context_dict = {}
    context_dict['number_of_papers'] = Paper.objects.all().count()
    context_dict['upload_form'] = PaperForm()
    return context_dict
