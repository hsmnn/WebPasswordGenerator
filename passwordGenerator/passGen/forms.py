from django import forms

class PassForm(forms.Form):
    length = forms.IntegerField(max_value = 94, min_value = 8, required = True, initial = 10)