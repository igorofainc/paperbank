# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import paper.utils.model_utils


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0003_auto_20160803_0819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='subjects',
            new_name='subject',
        ),
        migrations.AlterField(
            model_name='paper',
            name='paper_file',
            field=models.FileField(upload_to=paper.utils.model_utils.uploaded_paper_name),
        ),
    ]
