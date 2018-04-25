from django.conf.urls import url

from .views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
    # restaurant_detail_view,
    # restaurant_create_view,
    # restaurant_create_modal_view
)

urlpatterns = [
    url(r'^$', RestaurantListView.as_view(), name='list'),
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'),
    # url(r'^restaurants/create/$', restaurant_create_view),
    # url(r'^restaurants/create/$', restaurant_create_modal_view),
    # url(r'^restaurant_detail/(?P<slug>[\w-]+)/$', restaurant_detail_view)
]