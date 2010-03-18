from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db import models

from goonsay.apps.voting.managers import VoteManager

SCORES = (
    (u'+1', +1),
    (r'-1', -1),
)

class Vote(models.Model):
    """
    A vote on an object by a IP Address.
    """
    ip_address      = models.IPAddressField()
    content_type    = models.ForeignKey(ContentType)
    object_id       = models.PositiveIntegerField()
    object          = generic.GenericForeignKey('content_type', 'object_id')
    vote            = models.SmallIntegerField(choices=SCORES)

    objects = VoteManager()

    class Meta:
        db_table = 'votes'
        unique_together = (('ip_address', 'content_type', 'object_id'),)

    def __unicode__(self):
        return u'%s: %s on %s' % (self.ip_address, self.vote, self.object)

    def is_upvote(self):
        return self.vote == 1

    def is_downvote(self):
        return self.vote == -1
