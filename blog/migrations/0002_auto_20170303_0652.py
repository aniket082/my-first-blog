# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 06:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='past',
            name='author',
        ),
        migrations.DeleteModel(
            name='past',
        ),
    ]
