from haystack.indexes import *
from haystack import site

from goonsay.apps.goonsay.models import GoonSay

class GoonSayIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    def get_queryset(self):
        return GoonSay.objects.all().approved()

    def load_all_queryset(self):
        return GoonSay.objects.all().approved().select_related()

site.register(GoonSay, GoonSayIndex)
