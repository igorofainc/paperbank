from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'papers', views.get_papers, name='get_papers_api'),
]
