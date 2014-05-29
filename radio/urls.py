from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from radio.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index, name='index'),
    # url(r'^radio/', include('radio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^apps/radio/helm/', include(admin.site.urls)),
    url(r'^apps/radio/', include('stations.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
