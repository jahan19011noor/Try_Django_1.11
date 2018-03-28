# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view

def home(request):

# up to chapter 5: For your Reference
    # return HttpResponse("Home Page")
# up to chapter 5: For your Reference


# up to chapter 5: Rendering HTML
    html_ = """
        <!DOCTYPE html>
        <html lang=en>
        <head>
        </head>
        <body>
            <h1>This is the homepage HTML</h1>
            <p>The is the content for the homepage</p>
        </body>
        </html>
    """

    return HttpResponse(html_)


    # return render(request, "home.html", {"Title":"Homepage"})