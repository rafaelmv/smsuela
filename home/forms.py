from django.forms import ModelForm
from .models import Number


class NumberForm(ModelForm):
    class Meta:
        model = Number
        fields = ['phone_number']
