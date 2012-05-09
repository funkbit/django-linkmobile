from django.conf.urls.defaults import *

urlpatterns = patterns('djlinkmobile.views',
    url(r'^callback/$', 'callback', name='djlinkmobile-callback'),
)
