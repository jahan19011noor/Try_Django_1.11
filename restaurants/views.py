import random
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .forms import RestaurantCreateForm, RestaurantCreateModelForm

from .models import Restaurant

class RestaurantListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user)

class RestaurantDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user)

class RestaurantCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = RestaurantCreateModelForm
    template_name = 'forms.html'
    # success_url = '/restaurants/'
#         Chapter 25. The Extra Power of Django Model Forms
    success_message = "Restaurant created successfully!"

    def form_valid(self, form):
        restaurant = form.save(commit=False)

        restaurant.owner = self.request.user
        #         when not logged in the self.request.user gives the class AnonymousUser not the User that we want
        # restaurant.save()
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Add Restaurant"
        return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantCreateModelForm
    template_name = 'forms.html'

    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Restaurant: {}'.format(self.get_object().name)
        return context

class RestaurantDetailUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = RestaurantCreateModelForm
    template_name = 'restaurants/detail-update.html'
    success_message = "Restaurant updated successfully!"

    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantDetailUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Restaurant: {}'.format(self.get_object().name)
        return context