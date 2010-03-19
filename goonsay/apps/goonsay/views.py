from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.views.decorators.cache import cache_control, never_cache

from goonsay.apps.goonsay.models import GoonSay
from goonsay.apps.goonsay.forms import GoonSayForm

@never_cache
def random(request):
    qs = GoonSay.objects.order_by('?').approved()[:1]
    if len(qs):
        return render_to_response('goonsay/goonsay_detail.html',
            {'object': qs[0]},
            context_instance=RequestContext(request))
    else:
        raise Http404

def add(request):
    if request.method == 'POST':
        post_vars = request.POST.copy()
        post_vars['added_ip'] = request.META['REMOTE_ADDR']
        qs = GoonSay.objects.filter(text=post_vars['text'])
        if len(qs):
            return HttpResponseRedirect(qs[0].get_absolute_url())
        form = GoonSayForm(post_vars, request.FILES)
        if form.is_valid():
            new_object = form.save()
            return HttpResponseRedirect(new_object.get_absolute_url())
    else:
        form = GoonSayForm()

    return render_to_response('goonsay/goonsay_form.html',
        {'form': form},
        context_instance=RequestContext(request))
