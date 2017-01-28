"""
App to manage users for paperbank.
The users are logged in with facebook,
We manage other functionality in this app.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^logout', views.sign_out, name='sign_out'),
]

