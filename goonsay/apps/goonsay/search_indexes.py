import datetime

from haystack.indexes import *
from haystack import site

from goonsay.apps.goonsay.models import GoonSay

class GoonSayIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)
    added = DateTimeField(model_attr='added')

    def get_queryset(self):
        return GoonSay.objects.filter(added__lte=datetime.datetime.now())

site.register(GoonSay, GoonSayIndex)
