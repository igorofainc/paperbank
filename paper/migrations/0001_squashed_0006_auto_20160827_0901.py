# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-12 06:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import paper.utils.model_utils


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# paper.migrations.0006_auto_20160827_0901

def subject_to_tag(apps, schema_editor):
    """
    Migrates the subjects data to the tag model
    """
    Paper = apps.get_model('paper', 'Paper')
    Subject = apps.get_model('paper', 'Subject')
    Tag = apps.get_model('paper', 'Tag')

    papers = Paper.objects.all()

    for paper in papers:
        try:
            with transaction.atomic():
                paper.tags.create(name=paper.subject.name)
                paper.save()
        except IntegrityError:
            tag = Tag.objects.filter(name=paper.subject.name).first()
            paper.tags.add(tag)
            paper.save()
            print "Tag already exists"


def reverse_subject_to_tag(apps, schema_editor):
    """
    Reversing the actions done by the function subject_to_tag
    """
    Paper = apps.get_model('paper', 'Paper')
    Subject = apps.get_model('paper', 'Subject')
    Tag = apps.get_model('paper', 'Tag')


    papers = Paper.objects.all()

    for paper in papers:
        tag = paper.tags.first()
        try:
            with transaction.atomic():
                paper.subject = Subject.objects.create(name=tag.name)
                paper.save()
        except IntergrityError:
            subject = Subject.objects.filter(name=tag.name)
            paper.subject = subject
            paper.save()
            print "Subject already exists"








class Migration(migrations.Migration):

    replaces = [(b'paper', '0001_initial'), (b'paper', '0002_auto_20160803_0801'), (b'paper', '0003_auto_20160803_0819'), (b'paper', '0004_auto_20160803_0907'), (b'paper', '0005_paper_created_date'), (b'paper', '0006_auto_20160827_0901')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('paper_file', models.FileField(upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='paper',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paper.Subject'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='paper_file',
            field=models.FileField(upload_to=paper.utils.model_utils.uploaded_paper_name),
        ),
        migrations.AddField(
            model_name='paper',
            name='created_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 8, 3, 9, 11, 31, 937273)),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='paper',
            name='tags',
            field=models.ManyToManyField(to=b'paper.Tag'),
        ),
        migrations.RunPython(
            code=subject_to_tag,
            reverse_code=reverse_subject_to_tag,
        ),
        migrations.RemoveField(
            model_name='paper',
            name='subject',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
