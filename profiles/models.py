from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from .utils import code_generator

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

    def followers_list(self, request_user):
        user_model = get_user_model()

        followers_list = user_model.objects.filter(profile__following=request_user)
        return followers_list

    def toggle_follow(self, request_user, username_to_toggle):
        following_list = request_user.profile.following.all()

        user_to_toggle = Profile.objects.get(user__username__exact=username_to_toggle).user
        is_following = False
        if user_to_toggle in following_list:
            request_user.profile.following.remove(user_to_toggle)
        else:
            request_user.profile.following.add(user_to_toggle)
            is_following = True

        return is_following

class Profile(models.Model):
    user        = models.OneToOneField(User) #user.profile accesses profile and reverse
    following   = models.ManyToManyField(User, related_name='followers', blank=True)
    activation_key = models.CharField(max_length=120, blank=True, null=True)
    activated   = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username

    def send_activate_email(self):
        if not self.activated:
            self.activation_key = code_generator()
            self.save()

            subject = 'Activate User Email'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = "Active your email here: ".format(self.activation_key)
            recipient_list = [self.user.email]
            html_message = 'Active your email here: {}'.format(self.activation_key)
            print(html_message)
            send_mail = False

            path_ = reverse('activate-user', kwargs={"code": self.activation_key})
            html_message = 'Active your email here: {}'.format(path_)
            print(html_message)

            # sent_mail = send_mail(
            #                         subject,
            #                         message,
            #                         from_email,
            #                         recipient_list,
            #                         fail_silently=False,
            #                         html_message=html_message
            #                     )
            return send_mail

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        the_super_user_profile = Profile.objects.get_or_create(user__id=1)[0]
        profile.following.add(the_super_user_profile.user)
        the_super_user_profile.following.add(instance)

post_save.connect(post_save_user_receiver, sender=User)