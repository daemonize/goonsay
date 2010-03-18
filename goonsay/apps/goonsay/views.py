from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect

from goonsay.apps.goonsay.models import GoonSay
from goonsay.apps.goonsay.forms import GoonSayForm

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
        form = GoonSayForm(post_vars, request.FILES)
        if form.is_valid():
            new_object = form.save()
            return HttpResponseRedirect(new_object.get_absolute_url())
    else:
        form = GoonSayForm()

    return render_to_response('goonsay/goonsay_form.html',
        {'form': form},
        context_instance=RequestContext(request))
