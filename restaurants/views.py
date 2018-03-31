import random
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import Restaurant

def restaurang_list_view(request):

    querySet = Restaurant.objects.all()

    template_name = 'restaurants/restaurant_list.html'
    context = {'obj_list': {'title': 'Restaurant List', 'restaurants': querySet}}
    return render(request, template_name=template_name, context=context)

class RestaurantListView(ListView):
    # built in attributes of ListView:
    # queryset      // not querySet or QuerySet
    # template_name // not template_Name or templateName
    # object_list   // not object_List or objectList
    #           // object_list gets assigned automatically with queryset
    #           // object_list gets assigned dynaically assigned to the context dict
    #           // thus, object_list gets sent to the html and has to be received with the same name there

    # overriding queryset and template_name
    queryset = Restaurant.objects.all()
    template_name = 'restaurants/restaurant_view.html'
    # if not overridden then it will show errro 'template_name' missing or 'QuerySet' missing

class SylhetiRestaurantListView(ListView):

    queryset = Restaurant.objects.filter(catagory__iexact='sylheti')
    template_name = 'restaurants/restaurant_view.html'

class Star5RestaurantListView(ListView):

    queryset = Restaurant.objects.filter(catagory__icontains='5 Star')
    template_name = 'restaurants/restaurant_view.html'

class Star3RestaurantListView(ListView):

    queryset = Restaurant.objects.filter(catagory__startswith='3 Star')
    template_name = 'restaurants/restaurant_view.html'

class SearchRestaurantListView(ListView):
    template_name = 'restaurants/restaurant_view.html'

    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get('slug')

        if slug:
            if slug=='list':
                queryset = Restaurant.objects.all()
            else:
                if '_' in slug:
                    slug = slug.replace("_", " ")

                queryset = Restaurant.objects.filter(
                    Q(catagory__iexact=slug) |
                    Q(catagory__icontains=slug)
                )
        else:
            queryset = Restaurant.objects.all()

        return queryset