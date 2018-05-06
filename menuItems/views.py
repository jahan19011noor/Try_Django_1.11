from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import MenuItem
from .forms import MenuItemCreateModelForm

class MenuItemListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        queryset = MenuItem.objects.filter(user=self.request.user)
        return queryset

class MenuItemDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return MenuItem.objects.filter(user=self.request.user)

class MenuItemCreateView(LoginRequiredMixin, CreateView):
    form_class = MenuItemCreateModelForm
    template_name = 'forms.html'

    def form_valid(self, form):
        menuItem = form.save(commit=False)

        menuItem.user = self.request.user

        return super(MenuItemCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(MenuItemCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Menu Item'
        return context

    def get_form_kwargs(self, **kwargs):
        kwargs = super(MenuItemCreateView, self).get_form_kwargs(**kwargs)
        kwargs['user'] = self.request.user
        return kwargs


class MenuItemUpdateView(LoginRequiredMixin, UpdateView):
    form_class = MenuItemCreateModelForm
    template_name = 'forms.html'

    def get_queryset(self):
        return MenuItem.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(MenuItemUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Menu Item: {}'.format(self.get_object().name)
        return context

    def get_form_kwargs(self, **kwargs):
        kwargs = super(MenuItemUpdateView, self).get_form_kwargs(**kwargs)
        kwargs['user'] = self.request.user
        return kwargs

class MenuItemDetailUpdateView(LoginRequiredMixin, UpdateView):
    form_class = MenuItemCreateModelForm
    template_name = 'menuItems/detail-update.html'

    def get_queryset(self):
        return MenuItem.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(MenuItemDetailUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Menu Item: {}'.format(self.get_object().name)
        return context

    def get_form_kwargs(self, **kwargs):
        kwargs = super(MenuItemDetailUpdateView, self).get_form_kwargs(**kwargs)
        kwargs['user'] = self.request.user
        return kwargs