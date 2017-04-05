from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


from .models import Paper, Tag
from .utils.ui_utils import get_main_page_context_dict



# Create your views here.
def landing(request):
    """
    This renders the first page that the user sees when
    visiting the application.
    Just rendering the page.
    """
    return render(request, 'landing_page.html')


def main(request):
    """
    Main page 
    Lists the papers current in the database,
    """
    context_dict = {}
    papers = Paper.objects.all().order_by('-created_date')

    context_dict['papers'] = papers
    context_dict.update(get_main_page_context_dict())
    return render(request, 'main_page.html', context_dict)


def search(request):
    """
    Searches through the papers and find
    the most appropriate 
    """
    context_dict = {}
    question = request.GET.get('q', '')
    page = request.GET.get('page', 1)

    results = Paper.objects.filter(name__icontains=question).order_by('-created_date')
    context_dict['papers'] = results
    context_dict.update(get_main_page_context_dict())
    return render(request, 'main_page.html', context_dict)

def filter_by_tag(request, tag_name):
    """
    This filters through the papers basing
    on the given tag 
    """
    context_dict = {}
    tag = Tag.objects.filter(name=tag_name)

    if not tag:
        return redirect(reverse('main_page'))

    results = Paper.objects.filter(tags=tag).order_by('-created_date')
    context_dict['papers'] = results
    context_dict.update(get_main_page_context_dict())
    return render(request, 'main_page.html', context_dict)


