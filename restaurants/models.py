# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name        = models.CharField(max_length=100)
    location    = models.CharField(max_length=255, null=True, blank=True)