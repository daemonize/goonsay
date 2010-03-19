from django.template import Library

from goonsay.apps.goonsay.models import GoonSay

register = Library()

@register.inclusion_tag('goonsay/stats.html')
def show_goonsay_stats():
    approved = len(GoonSay.objects.all().approved())
    pending = len(GoonSay.objects.all().pending())
    return {'approved': approved, 'pending': pending}

@register.inclusion_tag('render_paginator.html', takes_context=True)
def render_paginator(context, first_last_amount=2, before_after_amount=4):
    page_obj = context['page_obj']
    paginator = context['paginator']
    page_numbers = []

    # Pages before current page
    if page_obj.number > first_last_amount + before_after_amount:
        for i in range(1, first_last_amount + 1):
            page_numbers.append(i)

        for i in range(page_obj.number - before_after_amount, page_obj.number):
            page_numbers.append(i)

    else:
        for i in range(1, page_obj.number):
            page_numbers.append(i)

    # Current page and pages after current page
    if page_obj.number + first_last_amount + before_after_amount < paginator.num_pages:
        for i in range(page_obj.number, page_obj.number + before_after_amount + 1):
            page_numbers.append(i)

        for i in range(paginator.num_pages - first_last_amount + 1, paginator.num_pages + 1):
            page_numbers.append(i)

    else:
        for i in range(page_obj.number, paginator.num_pages + 1):
            page_numbers.append(i)

    return {
        'paginator': paginator,
        'page_obj': page_obj,
        'page_numbers': page_numbers
    }
