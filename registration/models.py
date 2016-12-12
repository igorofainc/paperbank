from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Registrant(models.Model):
    """
    The person being registered 
    """
    name = models.CharField(max_length=40, help_text="Your Name")
    email = models.EmailField(help_text="Your Email")
    phone_number = models.CharField(max_length=12, help_text="Phone number")
    school = models.CharField(max_length=50, help_text="Your previous school") # Previous school attended
    description = models.TextField(help_text="Describe about your education and where you want to study.") # Brief descritpion of where a students wants to study

    def __str__(self):
        return self.name
