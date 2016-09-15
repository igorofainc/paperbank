from __future__ import unicode_literals
from django.db import models


from .model_tools import uploaded_paper_name 

# Create your models here.

class Tag(models.Model):
    """
    To be used as a way to filter through papers
    papers can have many tags or hashtags
    """
    name = models.CharField(max_length=40, unique=True  )

    def __str__(self):
        return '#' + self.name



class Paper(models.Model):
    """
    This is the main model to 
    hold the uploaded papers
    """
    name = models.CharField(max_length=50)
    paper_file = models.FileField(upload_to=uploaded_paper_name)
    created_date = models.DateTimeField(auto_now=True) 
        
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

