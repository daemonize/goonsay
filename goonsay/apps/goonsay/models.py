from django.db import models
from django.utils.translation  import ugettext_lazy as _

import gatekeeper
from djangoratings.fields import AnonymousRatingField

class GoonSay(models.Model):
    text = models.TextField(_('text'))
    added = models.DateTimeField(_('added'), auto_now_add=True)
    added_ip = models.IPAddressField(_('added by ip'))

    rating = AnonymousRatingField(range=5, can_change_vote=True)

    class Meta:
        verbose_name = _('goonsay')
        verbose_name_plural = _('goonsays')

    def __unicode__(self):
        return u'#%s' % self.id

    @models.permalink
    def get_absolute_url(self):
        return ('goonsay:detail', (), {'object_id': self.id})

gatekeeper.register(GoonSay)
