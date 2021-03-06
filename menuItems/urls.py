from django.conf.urls import url

from .views import (
    MenuItemListView,
    MenuItemDetailView,
    MenuItemCreateView,
    MenuItemUpdateView,
    MenuItemDetailUpdateView
)

urlpatterns = [
    url(r'^$', MenuItemListView.as_view(), name='list'),
    url(r'^create/$', MenuItemCreateView.as_view(), name='create'),
    # url(r'^(?P<slug>[\w-]+)/update/$', MenuItemUpdateView.as_view(), name='update'),
    # url(r'^(?P<slug>[\w-]+)/$', MenuItemDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', MenuItemDetailUpdateView.as_view(), name='detail'),
]