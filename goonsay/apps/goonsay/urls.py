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
        'django.views.generic.list_detail.object_list',
        {
            'queryset': GoonSay.objects.order_by('added').approved(),
            'paginate_by': 20,
            'extra_context': {'title': 'Browse'},
        },
        name='browse'
    ),
    url(
        r'^random/$',
        'goonsay.apps.goonsay.views.random',
        name='random',
    ),
    url(
        r'^top/$',
        'django.views.generic.list_detail.object_list',
        {
            'queryset': GoonSay.objects.select_score().order_by('-score').approved()[:100],
            'extra_context': {'title': 'Top 100'},
        },
        name='top',
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
        r'^(?P<object_id>\d+)/vote/(?P<direction>up|down|clear)/$',
        'goonsay.apps.voting.views.vote_on_object',
        {
            'model': GoonSay,
            'allow_xmlhttprequest': True,
            'template_name': 'goonsay/goonsay_detail.html',
            'extra_context': {'voting_confirm': True},
        },
        name='voting',
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
