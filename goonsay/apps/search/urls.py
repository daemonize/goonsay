from django.conf.urls.defaults import *

from haystack.views import SearchView
from goonsay.apps.search.forms import StyledSearchForm

urlpatterns = patterns('',
    url(r'^$', SearchView(form_class=StyledSearchForm), name='haystack_search'),
)
