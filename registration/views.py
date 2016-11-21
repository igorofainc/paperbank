"""
This app registers individuals,
In this case it registers students who want to be
registered
"""
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register(request):
    """
    Main function of the app, 
    should display a registration form and process it
    """
    return HttpResponse("About to be registered")
