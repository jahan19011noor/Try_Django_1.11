from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user        = models.OneToOneField(User) #user.profile accesses profile and reverse
    following   = models.ManyToManyField(User, related_name='followers', blank=True)
    activated   = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        the_super_user_profile = Profile.objects.get_or_create(user__id=1)[0]
        profile.following.add(the_super_user_profile.user)
        the_super_user_profile.following.add(instance)

post_save.connect(post_save_user_receiver, sender=User)