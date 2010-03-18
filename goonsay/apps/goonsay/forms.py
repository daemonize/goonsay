from django.forms import ModelForm

from goonsay.apps.goonsay.models import GoonSay

class GoonSayForm(ModelForm):
    class Meta:
        model = GoonSay
