from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, PasswordResetView

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^login/$', LoginView.as_view(), name='login_url'),
    url(r'^password_reset/$', PasswordResetView.as_view(), name='password_reset'),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
]