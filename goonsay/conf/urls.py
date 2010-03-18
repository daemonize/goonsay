from django.conf.urls.defaults import *

from haystack.views import SearchView
from haystack.forms import SearchForm

urlpatterns = patterns('',
    url(r'^admin/gatekeeper/', include('gatekeeper.urls')),
    url(
        r'^search/$',
        SearchView(form_class=SearchForm),
        name='haystack_search',
    ),
    url(
        r'^',
        include(
            'goonsay.apps.goonsay.urls',
            namespace='goonsay',
            app_name='goonsay'
        )
   ),
)
