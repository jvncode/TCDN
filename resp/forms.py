from django import forms

class Inputs(forms.Form):
    
    dominio = forms.URLField(label='Dominio', max_length=80, required=True, validators=())
    ip = forms.CharField(label='IP', max_length=15, required=False)