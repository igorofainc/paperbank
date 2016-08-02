from django.shortcuts import render
from django.http import HttpResponse

from .models import Paper
from .utils import get_page


# Create your views here.

def main(request):
    """
    This is the main page 
    where the main user lands
    """
    context_dict = {}
    papers = Paper.objects.all()
    page = request.GET.get('page', 1)

    context_dict['papers_page'] = get_page(papers, page)
    return render(request, 'main_page.html', context_dict)


def search(request):
    """
    Searches through the papers and find
    the most appropriate 
    """
    context_dict = {}
    question = request.GET.get('q', '')
    page = request.GET.get('page', 1)

    results = Paper.objects.filter(name__icontains=question)
    context_dict['papers_page'] = get_page(results, page)
    return render(request, 'main_page.html', context_dict)
