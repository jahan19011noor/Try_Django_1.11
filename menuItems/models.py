from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save

from trydjango.utils import unique_slug_generator
from restaurants.models import Restaurant

class MenuItem(models.Model):
    # relationship fields
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant  = models.ForeignKey(Restaurant)
    # menuItem fields
    name        = models.CharField(max_length=120)
    contents    = models.TextField(help_text='Separate each item by comma')
    excludes    = models.TextField(blank=True, null=True, help_text='Separate each item by comma')
    public      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menuItems:detail', kwargs={'slug': self.slug})

    def title(self):
        return self.name

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")

def menuItem_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(menuItem_pre_save_receiver, sender=MenuItem)