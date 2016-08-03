# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-03 08:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='paper',
            name='subjects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='paper.Subject'),
        ),
    ]