# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-02 19:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myppp', '0004_auto_20160102_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_ppp',
            name='author',
        ),
    ]
