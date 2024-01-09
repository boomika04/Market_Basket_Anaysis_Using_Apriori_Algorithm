from django import forms

class DesiredItemForm(forms.Form):
    desired_item = forms.CharField(label='Enter the desired item', max_length=100)
