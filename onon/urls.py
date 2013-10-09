from django.conf.urls.defaults import patterns, include, url
from onon.views import index

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'', include('lfluxproject.urls')),
    url(r'^api/autocomplete/', include('autocomplete_light.urls')),
)
