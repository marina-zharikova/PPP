# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accessory_type', models.CharField(default=b'', max_length=25, null=True, verbose_name='Accessory type', blank=True)),
            ],
            options={
                'verbose_name': 'Accessory type',
                'verbose_name_plural': 'Accessory types',
            },
        ),
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(default=b'', max_length=25, null=True, verbose_name='Size type', blank=True)),
                ('color_pic', colorful.fields.RGBColorField()),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='Fabric_subtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fabric_subtype', models.CharField(default=b'', max_length=25, null=True, verbose_name='Fabric subtype', blank=True)),
            ],
            options={
                'verbose_name': 'Fabric subtype',
                'verbose_name_plural': 'Fabric subtypes',
            },
        ),
        migrations.CreateModel(
            name='Fabric_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fabric_type', models.CharField(default=b'', max_length=25, null=True, verbose_name='Fabric type', blank=True)),
            ],
            options={
                'verbose_name': 'Fabric type',
                'verbose_name_plural': 'Fabric types',
            },
        ),
        migrations.CreateModel(
            name='Fringe_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fringe_type', models.CharField(default=b'', max_length=25, null=True, verbose_name='Fringe type', blank=True)),
            ],
            options={
                'verbose_name': 'Fringe type',
                'verbose_name_plural': 'Fringe types',
            },
        ),
        migrations.CreateModel(
            name='My_ppp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=b'media')),
                ('accessory_type', models.ForeignKey(blank=True, to='myppp.Accessory_type', null=True)),
                ('base_color', models.ForeignKey(related_name='base_color', blank=True, to='myppp.Colors', null=True)),
                ('border_color', models.ForeignKey(related_name='border_color', blank=True, to='myppp.Colors', null=True)),
                ('color1', models.ForeignKey(related_name='color1', blank=True, to='myppp.Colors', null=True)),
                ('color2', models.ForeignKey(related_name='color2', blank=True, to='myppp.Colors', null=True)),
                ('color3', models.ForeignKey(related_name='color3', blank=True, to='myppp.Colors', null=True)),
                ('fabric_subtype', models.ForeignKey(blank=True, to='myppp.Fabric_subtype', null=True)),
                ('fabric_type', models.ForeignKey(blank=True, to='myppp.Fabric_type', null=True)),
                ('fringe_type', models.ForeignKey(blank=True, to='myppp.Fringe_type', null=True)),
            ],
            options={
                'verbose_name': 'My PPP',
                'verbose_name_plural': 'My PPP',
            },
        ),
        migrations.CreateModel(
            name='Size_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size_type', models.CharField(default=b'', max_length=25, null=True, verbose_name='Size type', blank=True)),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Size',
            },
        ),
        migrations.AddField(
            model_name='my_ppp',
            name='size_type',
            field=models.ForeignKey(blank=True, to='myppp.Size_type', null=True),
        ),
        migrations.AddField(
            model_name='fabric_subtype',
            name='fabric_type',
            field=models.ForeignKey(blank=True, to='myppp.Fabric_type', null=True),
        ),
    ]
