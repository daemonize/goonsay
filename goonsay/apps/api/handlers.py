from piston.handler import AnonymousBaseHandler, BaseHandler
from piston.utils import rc, throttle, require_extended

from goonsay.apps.goonsay.models import GoonSay

class GoonSayHandler(BaseHandler):
    anonymous = True
    allowed_methods = ('GET', 'POST')
    fields = ('text', 'id', 'content_size', 'score')
    model = GoonSay

    @classmethod
    def score(self, goonsay):
        return goonsay.get_score()

    @classmethod
    def content_size(self, goonsay):
        return len(goonsay.text)
    
    def read(self, request, id=None, action=None):
        if action and id:
            return rc.NOT_IMPLEMENTED
        elif action == 'random':
            return GoonSay.objects.order_by('?').approved()[:1][0]
        elif action == 'top':
            return GoonSay.objects.select_score().order_by('-score').approved()[:100]
        elif action == 'latest':
            return GoonSay.objects.order_by('-added').approved()[:10]
        elif id:
            goonsay = GoonSay.objects.get(pk=id)
            return goonsay
        return GoonSay.objects.all().approved()

    @throttle(5, 10*60, 'create_goonsay')
    def create(self, request, id=None, action=None):
        if id:
            return rc.NOT_IMPLEMENTED
        if action:
            return rc.NOT_IMPLEMENTED

        attrs = self.flatten_dict(request.data)

        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            item = GoonSay(
                    text=attrs['text'],
                    added_ip=request.META['REMOTE_ADDR'],
                    )
            item.save()
            return item
