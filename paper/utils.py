"""
Main utils for the paper app
"""
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Paper


def get_page(papers, page):
    """
    Returns the page to be displayed with 
    a paginated system, The number of papers per page should be configured
    in the project settings
    """
    paginator = Paginator(papers, settings.PAPERS_PER_PAGE)

    try:
        papers_page = paginator.page(page)
    except PageNotAnInteger:
        papers_page = paginator.page(1)
    except EmptyPage:
        papers_page = paginator.page(paginator.num_pages)

    return papers_page


def get_main_page_context_dict():
    """
    Returns values that are rendered on the
    main application page.
    """
    context_dict = {}
    context_dict['number_of_papers'] = Paper.objects.all().count()
    return context_dict
