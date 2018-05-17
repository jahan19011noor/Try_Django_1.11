from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView, CreateView
from restaurants.models import Restaurant
from menuItems.models import MenuItem
from .models import Profile
from .forms import RegisterForm

User = get_user_model()

def activate_user_view(request, code=None, *args, **kwargs):
    if code:
        profile_qs = Profile.objects.filter(activation_key=code)
        if profile_qs.exists() and profile_qs.count() == 1:
            profile = profile_qs.first()
            if not profile.activated:

                user_ = profile.user
                user_.is_active = True
                user_.save()
                profile.activated = True
                profile.activation_key = None
                profile.save()
                return redirect("/login/")
    return redirect("/login/")

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect('/login/')
        return super(RegisterView,self).dispatch(*args,**kwargs)

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

        context['following'] = Profile.objects.following_list(user)
        context['suggested'] = Profile.objects.suggested_list(user)
        context['followers'] = Profile.objects.followers_list(user)

        request_user = self.request.user
        request_user_following_list = []

        if user != self.request.user:
            request_user_following_list = request_user.profile.following.all()

        is_following = False
        if user in request_user_following_list:
            is_following = True

        context['is_following'] = is_following

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

class ToggleFollowProfileView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        username = self.kwargs.get('username')

        toggle_follow = Profile.objects.toggle_follow(user, username)

        return redirect("/profiles/{}/".format(username))