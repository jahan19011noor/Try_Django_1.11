import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import Restaurant

def restaurang_list_view(request):

    querySet = Restaurant.objects.all()

    template_name = 'restaurants/restaurant_list.html'
    context = {'obj_list': {'title': 'Restaurant List', 'restaurants': querySet}}
    return render(request, template_name=template_name, context=context)