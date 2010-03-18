from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^admin/gatekeeper/', include('gatekeeper.urls')),
    url(r'^search/', include('goonsay.apps.search.urls')),
    url(
        r'^',
        include(
            'goonsay.apps.goonsay.urls',
            namespace='goonsay',
            app_name='goonsay'
        )
   ),
)
