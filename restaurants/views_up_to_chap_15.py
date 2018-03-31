import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# up to chapter 12: Class Based Views
class ContactView(View):
    def get(self, request, *args, **kwargs):
        print kwargs
        return render(request, "contact.html", {})
# up to chapter 12: Class Based Views

# up to chapter 13: Template View
class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(*args, **kwargs)
        print context

        num = random.randint(0, 10000000)
        list_of_values = ["one", "two", "three"]
        context = {
            "title": "Home 1", "show_the_random_number": True, "num": num, "values": list_of_values
        }

        return context

class AboutTemplateView(TemplateView):
    template_name = 'about.html'

class ContactTemplateView(TemplateView):
    template_name = 'contact.html'
# up to chapter 13: Template View