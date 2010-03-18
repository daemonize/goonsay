from django.conf.urls.defaults import *

from goonsay.apps.goonsay.models import GoonSay

urlpatterns = patterns('',
    url(
        r'^latest/$',
        'django.views.generic.list_detail.object_list',
        {
            'queryset': GoonSay.objects.order_by('-added').approved()[:10],
            'extra_context': {'title': 'Latest'},
        },
        name='latest',
    ),
    url(
        r'^browse/$',
        'goonsay.apps.goonsay.views.browse',
        name='browse'
    ),
    url(
        r'^browse/(?P<page>[0-9(?:last)]+)/$',
        'django.views.generic.list_detail.object_list',
        {
            'queryset': GoonSay.objects.order_by('added').approved(),
            'paginate_by': 25,
            'extra_context': {'title': 'Browse'},
        },
        name='browse-paged',
    ),
    url(
        r'^random/$',
        'goonsay.apps.goonsay.views.random',
        name='random',
    ),
    url(
        r'^add/$',
        'goonsay.apps.goonsay.views.add',
        name='add',
    ),
    url(
        r'^(?P<object_id>\d+)/$',
        'django.views.generic.list_detail.object_detail',
        {
            'queryset': GoonSay.objects.all(),
        },
        name='detail',
    ),
    url(
        r'^$',
        'django.views.generic.simple.direct_to_template',
        {
            'template': 'base.html',
        },
        name='index',
    )
)
