from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from restaurants.models import Restaurant
from menuItems.models import MenuItem

User = get_user_model()

class ProfileDetailVeiw(DetailView):
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

        menuItem_qs = MenuItem.objects.filter(user=user).exists()
        if restaurant_qs.exists() and menuItem_qs:
            context['restaurants'] = restaurant_qs
        return context