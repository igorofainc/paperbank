from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Registrant(models.Model):
    """
    The person being registered 
    """
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    school = models.CharField(max_length=50) # Previous school attended
    description = models.TextField() # Brief descritpion of where a students wants to study

    def __str__(self):
        return self.name
