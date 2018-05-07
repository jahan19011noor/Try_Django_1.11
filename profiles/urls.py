from django.conf.urls import url

from .views import ProfileDetailVeiw

urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailVeiw.as_view(), name='detail')
]