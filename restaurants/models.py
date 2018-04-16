# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

# Create your models here.
class Restaurant(models.Model):
    name            = models.CharField(max_length=100)
    location        = models.CharField(max_length=255, null=True, blank=True)
    catagory        = models.CharField(max_length=255, null=True, blank=True)
    timestamp       = models.DateTimeField(auto_now_add=True)   # Saves automatically and does not allow to make changes
    updated         = models.DateTimeField(auto_now=True)       # Saves automatically and does not allow to make changes
    slug            = models.SlugField(null=True, blank=True)
    # my_date_field   = models.DateTime(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


def r_pre_save_receiver(sender, instance, *args, **kwargs):
    print ('saving..')
    print (instance.timestamp)
    if not instance.slug:               #always do pre_save
        instance.slug = unique_slug_generator(instance)

# def r_post_save_receiver(sender, instance, *args, **kwargs):
#     print ('saved..')
#     print (instance.timestamp)
#     # instance.save()                     #not a recommanded way to save because it will run into an infinite loop as save() will recall post_save()
#     if not instance.slug:                 #this will never be called because the presave will already set the instance.slug, so infinite loop will be avoided
#         instance.slug = unique_slug_generator(instance)
#         instance.save()

pre_save.connect(r_pre_save_receiver, sender=Restaurant)
# post_save.connect(r_post_save_receiver, sender=Restaurant)