from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    """
    This is the main page 
    where the main user lands
    """
    return HttpResponse("This is the ")
