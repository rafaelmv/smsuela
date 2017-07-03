from django import forms
from .models import Number, Message


class NumberForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = ['phone_number']
        labels = {
            'phone_number': 'Número de teléfono (12 dígitos)'
        }

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        return '+' + data


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields =  ['text_message']
        labels = {
            'text_message': 'Tu mensaje'
        }

#class MessageForm(forms.Form):
#    body_message = forms.CharField(label='Tu mensaje', max_length=160, required=False)
