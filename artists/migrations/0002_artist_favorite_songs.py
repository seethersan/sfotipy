# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='favorite_songs',
            field=models.ManyToManyField(blank=True, related_name='is_favorite_to', to='tracks.Track'),
        ),
    ]
