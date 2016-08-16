""" The paper app urls """

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.landing, name='landing_page'),
    url(r'^papers$', views.main, name='main_page'),
    url(r'^search', views.search, name='search'),
]

