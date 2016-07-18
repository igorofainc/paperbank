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
