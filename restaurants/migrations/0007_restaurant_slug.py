# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_auto_20180331_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]