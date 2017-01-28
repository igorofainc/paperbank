from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.core.urlresolvers import reverse


# Create your views here.

def sign_out(request):
    """
    Signs out a paperbank logged in user,
    """
    logout(request)
    return redirect(reverse('main_page'))
