# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view

def home(request):

    return HttpResponse("Home Page")
    # return render(request, "home.html", {"Title":"Homepage"})