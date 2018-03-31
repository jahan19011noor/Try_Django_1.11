"""trydjango1_11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# up to chapter 12: Class Based Views
# from restaurants.views import home, contact, about
# up to chapter 12: Class Based Views

# up to chapter 15: More on Model Fields
# from restaurants.views import ContactView, \
#     ContactTemplateView, HomeTemplateView, AboutTemplateView
# up to chapter 15: More on Model Fields

from django.views.generic import TemplateView
from restaurants.views import restaurang_list_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', home),

# up to chapter 10: Include Template Tag
    # url(r'^contact/$', contact),
# # up to chapter 10: Include Template Tag

# up to chapter 12: Class Based Views
    # url(r'^contact/(?P<id>\d+)/$', ContactView.as_view()),    url having regurlar expression
    # url(r'^contact/$', ContactView.as_view()),
    # url(r'^about/$', about),
# up to chapter 12: Class Based Views

# up to chapter 13: Template View
#     url(r'^$', HomeTemplateView.as_view()),

    # these url are not needed unless we customize any function of the TemplateView class
    # url(r'^about/$', AboutTemplateView.as_view()),
    # url(r'^contact/$', ContactTemplateView.as_view()),
    # these url are not needed unless we customize any function of the TemplateView class

    # so we can replace them with
#     url(r'^about/$', TemplateView.as_view(template_name='about.html')),
#     url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
    # so we can replace them with

# up to chapter 13: Template View

# up to chapter 15: More on Model Fields

    # url(r'^$', HomeTemplateView.as_view()),
    # url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    # url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),

# up to chapter 15: More on Model Fields

    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
    url(r'^restaurants/$', restaurang_list_view)
]
# .as_view() creates an instance fo the class ContactView so that the class can be used