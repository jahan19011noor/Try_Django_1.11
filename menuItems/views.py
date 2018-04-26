from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from .models import MenuItem
from .forms import MenuItemCreateModelForm

class MenuItemListView(ListView):
    def get_queryset(self):
        queryset = MenuItem.objects.filter(user=self.request.user)
        return queryset

class MenuItemDetailView(DeleteView):
    template_name = 'menuItems/menuitem_detail.html'
    queryset = MenuItem.objects.all()

class MenuItemCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
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

class MenuItemUpdateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = MenuItemCreateModelForm
    template_name = 'forms.html'

    def form_valid(self, form):
        menuItem = form.save(commit=False)

        menuItem.user = self.request.user

        return super(MenuItemUpdateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(MenuItemUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Menu Item'
        return context
