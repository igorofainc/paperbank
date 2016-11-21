"""
Urls for the registration app, 
This app registers individuals ( in this case student who want to study abroad)
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.register, name='register'),
]
