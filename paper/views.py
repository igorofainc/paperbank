from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Paper, Tag
from .forms import PaperForm
from .utils.ui_utils import get_main_page_context_dict
from .utils.paper_management_utils import get_storage_size


# Create your views here.
def landing(request):
    """
    This renders the first page that the user sees when
    visiting the application.
    Just rendering the page.
    """
    print "The user is: %s" % request.user
    return render(request, 'landing_page.html')


def main(request):
    """
    Main page 
    Lists the papers current in the database,
    """
    context_dict = {}
    papers = Paper.objects.all().order_by('-created_date')

    context_dict['papers'] = Paper.objects.all()
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



@login_required
@require_POST
def upload_paper(request):
    """
    This view allow users to upload paper files, 
    """
    paper_form = PaperForm(request.POST, request.FILES)
    
    if paper_form.is_valid():
        paper_form.save()
        return redirect(reverse('main_page'))

    return HttpResponse("Invalid form");
    


def storage_size(request):
    """
    Returns the size of the files stored in megabytes,

    TODO: This should be moved to a management app, or the dashboard 
    """
    return HttpResponse('The size is: %s mb' % get_storage_size(size='mb'))
 

