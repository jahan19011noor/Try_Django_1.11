from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

class ProfileManager(models.Manager):
    def following_and_suggested(self, request_user):
        following_list = request_user.profile.following.all()
        suggested_list = []
        for fellow in following_list:
            fellow_following_list = fellow.profile.following.all()
            for item in fellow_following_list:
                if item not in suggested_list and item not in following_list and item != request_user:
                    suggested_list.append(item)
        return following_list, suggested_list

class Profile(models.Model):
    user        = models.OneToOneField(User) #user.profile accesses profile and reverse
    following   = models.ManyToManyField(User, related_name='followers', blank=True)
    activated   = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        the_super_user_profile = Profile.objects.get_or_create(user__id=1)[0]
        profile.following.add(the_super_user_profile.user)
        the_super_user_profile.following.add(instance)

post_save.connect(post_save_user_receiver, sender=User)