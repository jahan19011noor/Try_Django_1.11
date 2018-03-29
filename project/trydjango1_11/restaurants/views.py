import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def home(request):
    num = random.randint(0, 10000000)
    list_of_values = ["one", "two", "three"]

    return render(request, "home.html", {"title":"Homepage", "show_the_random_number": True, "num": num, "values": list_of_values})

def contact(request):
    num = random.randint(0, 10000000)
    list_of_values = ["one", "two", "three"]

    return render(request, "contact.html", {"title":"Home 1", "show_the_random_number": True, "num": num, "values": list_of_values})

def about(request):
    num = random.randint(0, 10000000)
    list_of_values = ["one", "two", "three"]

    return render(request, "about.html", {"title":"Home 2", "show_the_random_number": True, "num": num, "values": list_of_values})


class ContactView(View):
    def get(self, request, *args, **kwargs):
        print kwargs
        return render(request, "contact.html", {})