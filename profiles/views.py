from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView
from restaurants.models import Restaurant
from menuItems.models import MenuItem
from .models import Profile

User = get_user_model()

class ProfileDetailVeiw(LoginRequiredMixin, DetailView):
    template_name = 'profiles/user_detail.html'
    
    def get_object(self):
        username = self.kwargs.get('username')
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailVeiw, self).get_context_data(*args, **kwargs)
        user = context['user']
        query = self.request.GET.get('q')

        restaurant_qs = Restaurant.objects.filter(owner=user).search(query)

        following_list, suggested_list = Profile.objects.following_and_suggested(user)
        context['following'] = following_list
        context['suggested'] = suggested_list

        menuItem_qs = MenuItem.objects.filter(user=user).exists()

        if restaurant_qs.exists() and menuItem_qs:
            context['restaurants'] = restaurant_qs

        return context

class UnfollowProfileView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = request.user
        username = self.kwargs.get('username')
        user_to_unfollow = User.objects.get(username__exact=username)

        user.profile.following.remove(user_to_unfollow)

        return redirect("/profiles/{}/".format(user))

class FollowProfileView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = request.user
        username = self.kwargs.get('username')
        user_to_follow = User.objects.get(username__exact=username)

        user.profile.following.add(user_to_follow)

        return redirect("/profiles/{}/".format(user))