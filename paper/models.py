from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Paper(models.Model):
    """
    This is the main model to 
    hold the uploaded papers
    """
    name = models.CharField(max_length=50)
    paper_file = models.FileField(upload_to='uploads')

    def __str__(self):
        return self.name
