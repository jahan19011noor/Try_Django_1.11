# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20180330_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='catagory',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]