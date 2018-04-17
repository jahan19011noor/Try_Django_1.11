from django.conf.urls import url
from django.contrib import admin

from django.views.generic import TemplateView
from restaurants.views import (
    RestaurantListView,
    RestaurantDetailView,
    restaurant_detail_view
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
    url(r'^restaurants/$', RestaurantListView.as_view()),

    # after chapter 22. Slugs as URL Params
    url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),
    # after chapter 22. Slugs as URL Params
    url(r'^restaurant_detail/(?P<slug>[\w-]+)/$', restaurant_detail_view),
]