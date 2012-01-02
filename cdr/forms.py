from django import forms
from datetime import date
from django.forms.widgets import CheckboxSelectMultiple

DISPOSITIONS = (
 ('ALL','ALL'),
 ('FAILED','FAILED'),
 ('ANSWERED','ANSWERED'),
 ('NO ANSWER','NO ANSWER'),
 ('BUSY','BUSY'),
)

class CdrSearchForm(forms.Form):
    calldate_from = forms.DateField(initial=date.today(), required=False)
    calldate_to = forms.DateField(initial=date.today(), required=False)
    disposition = forms.CharField(widget=forms.Select(choices=DISPOSITIONS), required=False)
#    widget=forms.Select(choices=TITLE_CHOICES)
