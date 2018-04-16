import random
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import Restaurant

def restaurang_list_view(request):

    querySet = Restaurant.objects.all()

    template_name = 'restaurants/restaurant_view.html'
    context = {'obj_list': {'title': 'Restaurant List', 'restaurants': querySet}}
    return render(request, template_name=template_name, context=context)

class RestaurantListView(ListView):
    queryset = Restaurant.objects.all()

class RestaurantDetailView(DetailView):

    queryset = Restaurant.objects.all()
    def get_context_data(self, *args, **kwargs):
        # queries field_name = value - where field_name = url_param_name and value = value
        print(self.kwargs)
        context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)   # getting the super's get_context_data
        print(context)  # print the supers context
        return context  # have to return to complete overriding