from django.conf.urls import url
from django.contrib import admin

from django.views.generic import TemplateView
from restaurants.views import (
    RestaurantListView,
    RestaurantDetailView,
    restaurant_detail_view,
    restaurant_create_view,
    restaurant_create_modal_view,
    RestaurantCreateView
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
    url(r'^restaurants/$', RestaurantListView.as_view()),

    # after chapter 22. Slugs as URL Params
#     ---------------------- Forms ------------------ #
#     Chapter 24. Saving Data the Hard + Wrong Way

    # url(r'^restaurants/create/$', restaurant_create_view),
    # url(r'^restaurants/create/$', restaurant_create_modal_view),
    url(r'^restaurants/create/$', RestaurantCreateView.as_view()),
#     this url being before the slug url gets matched first and thus the url match succeeds
#     if placed below the slug url the url match will fail

#     ---------------------- Forms ------------------ #
    url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),
    # after chapter 22. Slugs as URL Params
    url(r'^restaurant_detail/(?P<slug>[\w-]+)/$', restaurant_detail_view),

]