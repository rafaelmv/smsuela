from django import forms
from .models import Number


class NumberForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = ['phone_number']

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        return '+' + data


class MessageForm(forms.Form):
    body_message = forms.CharField(label='Your message', max_length=153, required=False)
