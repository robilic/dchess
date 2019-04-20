import datetime
from django import forms
from django.core.exceptions import ValidationError

class Create(forms.Form):
	color = forms.ChoiceField(label='Color', required=True, widget=forms.RadioSelect, choices=[('1', 'white'), ('0', 'black')])
	description = forms.CharField(label='Description', required=True)
	challenger = forms.IntegerField(label='Challenger', required=True)	
