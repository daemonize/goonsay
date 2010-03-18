from django import forms
from django.utils.translation import ugettext_lazy as _

from haystack.forms import SearchForm

class StyledSearchForm(SearchForm):
    q = forms.CharField(
        required=False,
        label=_('Search'),
        widget=forms.TextInput(attrs={'class':'text'}),
    )
