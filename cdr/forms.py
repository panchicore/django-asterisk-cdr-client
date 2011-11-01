from django import forms
from datetime import date
class CdrSearchForm(forms.Form):
    calldate_from = forms.DateField(initial=date.today())
    calldate_to = forms.DateField(initial=date.today())
