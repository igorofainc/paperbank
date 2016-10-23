""" The paper app urls """

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.landing, name='landing_page'),
    url(r'^papers$', views.main, name='main_page'),
    url(r'^tag/(\w{0,50})$', views.filter_by_tag, name='filter_by_tag'),
    url(r'^search', views.search, name='search'),
]

