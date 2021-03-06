from django.db import models
from django.utils.translation  import ugettext_lazy as _

import gatekeeper

from goonsay.apps.goonsay.managers import VotedObjectsManager
from goonsay.apps.voting.models import Vote

class GoonSay(models.Model):
    text = models.TextField(_('text'), unique=True)
    added = models.DateTimeField(_('added'), auto_now_add=True)
    added_ip = models.IPAddressField(_('added by ip'))

    objects = VotedObjectsManager()

    class Meta:
        verbose_name = _('goonsay')
        verbose_name_plural = _('goonsays')

    def __unicode__(self):
        return u'#%s' % self.id

    @models.permalink
    def get_absolute_url(self):
        return ('goonsay:detail', (), {'object_id': self.id})

    def get_score(self):
        return Vote.objects.get_score(self)

gatekeeper.register(GoonSay)
