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
    # built in attributes of ListView:
    # queryset      // not querySet or QuerySet
    # template_name // not template_Name or templateName
    # object_list   // not object_List or objectList
    #           // object_list gets assigned automatically with queryset
    #           // object_list gets assigned dynaically assigned to the context dict
    #           // thus, object_list gets sent to the html and has to be received with the same name there

    # overriding queryset and template_name
    queryset = Restaurant.objects.all()
    # template_name = 'restaurants/restaurant_view.html'
    # if not overridden then it will show errro 'template_name' missing or 'QuerySet' missing

class RestaurantDetailView(DetailView):

    queryset = Restaurant.objects.all()
    # lets view the context that gets loaded by the Generic DetailView by default - overriding get_context_data() o super
    def get_context_data(self, *args, **kwargs):
        # queries field_name = value - where field_name = url_param_name and value = value
        print(self.kwargs)
        context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)   # getting the super's get_context_data
        print(context)  # print the supers context
        return context  # have to return to complete overriding

# overriding get_object for DetailView to query with "restaurant_id"
#     def get_object(self, *args, **kwargs):
#         print(self.kwargs)
#         rest_id = self.kwargs.get('restaurant_id')
#         obj = get_object_or_404(Restaurant, id=rest_id)
#         return obj
# overriding get_object for DetailView to query with "restaurant_id"

    #******* do not have to provide template_name because the default template name for DetailView is modelName_detail.html
    # template_name = 'restaurants/restaurant_detail.html'
