from django import forms

from .models import Paper

class PaperForm(forms.ModelForm):
    """
    Form for uploading papers
    """
    tags = forms.CharField(help_text="separate tags with a comma, ex: maths, ldk")

    class Meta:
       model = Paper
       exclude = ('created_date', 'tags')
