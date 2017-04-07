from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'papers/$', views.list_papers, name='get_papers_api'),
    url(r'papers/(?P<pk>[0-9]+)/$', views.paper_detail, name='paper_detail_api'),
    url(r'search/$', views.search, name='paper_search_api'),
    url(r'filter/$', views.filter_by_tag, name='filter_by_tag_api')
]

urlpatterns = format_suffix_patterns(urlpatterns)

