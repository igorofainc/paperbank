from django.forms import ModelForm

from .models import Paper

class PaperForm(ModelForm):
    """
    Form for uploading papers
    """
    class Meta:
       model = Paper
       exclude = ('created_date', 'tags')
