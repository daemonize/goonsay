from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication

from goonsay.apps.api.handlers import GoonSayHandler

auth = HttpBasicAuthentication(realm='GoonSay')
ad = { 'authentication': auth }

goonsay_resource = Resource(handler=GoonSayHandler)

urlpatterns = patterns('',
    url(r'^goonsays/$', goonsay_resource),
    url(r'^goonsays/(?P<id>\d+)/$', goonsay_resource),
    url(r'^goonsays/(?P<action>(?:random|top|latest))/$', goonsay_resource),
)
