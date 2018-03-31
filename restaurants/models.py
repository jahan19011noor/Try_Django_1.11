# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name            = models.CharField(max_length=100)
    location        = models.CharField(max_length=255, null=True, blank=True)
    catagory        = models.CharField(max_length=255, null=True, blank=True)
    timestamp       = models.DateTimeField(auto_now_add=True)   # Saves automatically and does not allow to make changes
    updated         = models.DateTimeField(auto_now=True)       # Saves automatically and does not allow to make changes
    # my_date_field   = models.DateTime(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.catagory