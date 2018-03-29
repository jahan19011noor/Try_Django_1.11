# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view

def home(request):

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

# up to chapter 6: Render a Django Template

    num = random.randint(0, 10000000)
    list_of_values = ["one", "two", "three"]

    return render(request, "base.html", {"title":"Homepage", "show_the_random_number": True, "num": num, "values": list_of_values})

# up to chapter 6: Render a Django Template