from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer

from paper.models import Paper
from paper.serializers import PaperSerializer
# Create your views here.

class JsonResponse(HttpResponse):
    """
    An HttpResponse that renders its content into Json
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JsonResponse, self).__init__(content, **kwargs)


def get_papers(request):
    """
    Returns json data for the 
    papers
    """
    papers = Paper.objects.all() 
    paper_serializer = PaperSerializer(papers, many=True)
    return JsonResponse(paper_serializer.data)
