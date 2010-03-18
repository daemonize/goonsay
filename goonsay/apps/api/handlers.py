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
    
    def read(self, *args, **kwargs):
        return super(GoonSayHandler, self).read(*args, **kwargs)

    @throttle(5, 10*60, 'create_goonsay')
    def create(self, request, id=None):
        if id:
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
