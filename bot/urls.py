"""
Configuring urls, 
Setting up endpoint for the messenger Webhooks to talk to (Post data to on change)
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.main),
]

