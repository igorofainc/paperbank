"""
This app registers individuals,
In this case it registers students who want to be
registered
"""
from django.shortcuts import render
from django.http import HttpResponse

from .forms import RegistrantForm
# Create your views here.

def register(request):
    """
    Main function of the app, 
    should display a registration form and process it
    """
    context_dict = {}
    registrant = RegistrantForm()

    if request.method == 'POST':
        registrant = RegistrantForm(request.POST)
        if registrant.is_valid():
            registrant.save()
            return HttpResponse("Thank you for registering, we will contact you soon")

    context_dict['form'] = registrant
    return render(request, 'register.html', context_dict)
