from rest_framework import serializers

from paper.models import Paper

class PaperSerializer(serializers.ModelSerializer):
    """
    Serializer for the Paper model class
    """
    class Meta:
        model = Paper
        fields = ('id', 'name', 'paper_file')
