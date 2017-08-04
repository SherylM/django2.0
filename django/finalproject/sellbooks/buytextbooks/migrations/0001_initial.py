# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textbooktitle', models.CharField(max_length=250)),
                ('textbookauthor', models.CharField(max_length=250)),
                ('textbookpublisher', models.CharField(max_length=250)),
                ('textbooklocation', models.CharField(max_length=400)),
                ('textbookimage', models.CharField(max_length=1000)),
            ],
        ),
    ]
