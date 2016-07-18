"""
Main utils for the paper app
"""
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


PAPERS_PER_PAGE = 20

def get_page(papers, page):
    """
    Returns the page to be displayed with 
    a paginated system
    """
    paginator = Paginator(papers, PAPERS_PER_PAGE)

    try:
        papers_page = paginator.page(page)
    except PageNotAnInteger:
        papers_page = paginator.page(1)
    except EmptyPage:
        papers_page = paginator.page(paginator.num_pages)

    return papers_page
