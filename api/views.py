from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from paper.models import Paper, Tag
from paper.serializers import PaperSerializer
# Create your views here.


@api_view(['GET'])
def list_papers(request, format=None):
    """
    Returns json data for the 
    papers
    """
    papers = Paper.objects.all() 
    paper_serializer = PaperSerializer(papers, many=True)
    return Response(paper_serializer.data)


@api_view(['GET'])
def paper_detail(request, pk, format=None):
    """
    List the details of a paper given an id
    """
    try:
        paper = Paper.objects.get(pk=pk)
    except Paper.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    paper_serializer = PaperSerializer(paper)
    return Response(paper_serializer.data)


@api_view(['GET'])
def search(request, format=None):
    """
    Searches for papers matching a given input
    """
    question = request.GET.get('q', '')

    results = Paper.objects.filter(name__icontains=question).order_by('-created_date')
    paper_serializer = PaperSerializer(results, many=True)
    return Response(paper_serializer.data)


@api_view(['GET'])
def filter_by_tag(request, format=None):
    """
    Returns the fields that match a given tag
    """
    tag_name = request.GET.get('tag', '')

    try:
        tag = Tag.objects.get(name=tag_name)
    except Tag.DoesNotExist:
        return Response([], status=status.HTTP_404_NOT_FOUND)

    results = Paper.objects.filter(tags=tag).order_by('-created_date')
    paper_serializer = PaperSerializer(results, many=True)
    return Response(paper_serializer.data)