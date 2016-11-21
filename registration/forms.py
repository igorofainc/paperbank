"""
Forms for the registration app
"""
from django.forms import ModelForm

from .models import Registrant


class RegistrantForm(ModelForm):
    """
    Form used for registering users
    """
    class Meta:
        model = Registrant
        exclude = ('',)
