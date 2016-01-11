# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myppp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_ppp',
            name='author',
            field=models.CharField(default=b'', max_length=25, null=True, verbose_name='Author', blank=True),
        ),
        migrations.AddField(
            model_name='my_ppp',
            name='name',
            field=models.CharField(default=b'', max_length=25, null=True, verbose_name='Name', blank=True),
        ),
        migrations.AlterField(
            model_name='my_ppp',
            name='color1',
            field=models.ForeignKey(related_name='color1', verbose_name=b'Additional color 1', blank=True, to='myppp.Colors', null=True),
        ),
        migrations.AlterField(
            model_name='my_ppp',
            name='color2',
            field=models.ForeignKey(related_name='color2', verbose_name=b'Additional color 2', blank=True, to='myppp.Colors', null=True),
        ),
        migrations.AlterField(
            model_name='my_ppp',
            name='color3',
            field=models.ForeignKey(related_name='color3', verbose_name=b'Additional color 3', blank=True, to='myppp.Colors', null=True),
        ),
    ]
