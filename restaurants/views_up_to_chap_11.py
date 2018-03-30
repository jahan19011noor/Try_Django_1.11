
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view
# def home(request):

# up to chapter 5: For your Reference
    # return HttpResponse("Home Page")
# up to chapter 5: For your Reference


# up to chapter 5: Rendering HTML
    # html_ = """
    #     <!DOCTYPE html>
    #     <html lang=en>
#     <head>
    #     </head>
    #     <body>
    #         <h1>This is the homepage HTML</h1>
    #         <p>The is the content for the homepage</p>
    #     </body>
    #     </html>
    # """
    #
    # return HttpResponse(html_)
# up to chapter 5: Rendering HTML

# up to chapter 6. Render a Django Template and 7. Render a Django Template and 8. Context in Django Templates

    # num = random.randint(0, 10000000)
    # list_of_values = ["one", "two", "three"]
    #
    # return render(request, "base.html", {"title":"Homepage", "show_the_random_number": True, "num": num, "values": list_of_values})

# up to chapter 6. Render a Django Template and 7. Render a Django Template and 8. Context in Django Templates

# up to chapter 8. Template Inheritance
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
# up to chapter 8. Template Inheritance