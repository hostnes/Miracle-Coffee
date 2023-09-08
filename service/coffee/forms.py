from django import forms
from .models import *


class SendCV(forms.Form):
    genders = (
        ('M', 'Man'),
        ('W', 'Women'),
        ('T', 'Trans')
    )
    name = forms.CharField(max_length=30)
    age = forms.CharField(max_length=3)
    gender = forms.ChoiceField(choices=genders)
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 5}))