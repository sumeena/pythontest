from django.conf.urls import patterns, include, url

from django.contrib import admin
from profiles.views import Register

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^register/$', Register.as_view())
)
