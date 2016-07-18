from django.shortcuts import render
from django.http import HttpResponse

from .models import Paper


# Create your views here.

def main(request):
    """
    This is the main page 
    where the main user lands
    """
    context_dict = {}
    context_dict['papers'] = Paper.objects.all()
    return render(request, 'main_page.html', context_dict)


def search(request):
    """
    Searches through the papers and find
    the most appropriate 
    """
    context_dict = {}
    question = request.GET.get('q', '')

    results = Paper.objects.filter(name__contains=question)
    context_dict['papers'] = results
    return render(request, 'main_page.html', context_dict)
