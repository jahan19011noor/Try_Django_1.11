from django.conf.urls import url

from .views import ProfileDetailVeiw, UnfollowProfileView, FollowProfileView

urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailVeiw.as_view(), name='detail'),
    url(r'^unfollow/(?P<username>[\w-]+)/$', UnfollowProfileView.as_view(), name='unfollow'),
    url(r'^follow/(?P<username>[\w-]+)/$', FollowProfileView.as_view(), name='follow'),
]