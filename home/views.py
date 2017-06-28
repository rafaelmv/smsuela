from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NumberForm, MessageForm
from .models import Number
from django.conf import settings
from django.views.generic import ListView

from twilio.rest import Client


client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

class NumberList(ListView):
    model = Number

    def get_context_data(self, **kwargs):
        context = super(NumberList, self).get_context_data(**kwargs)
        context['title'] = 'Números'
        return context


def index(request):

    all_numbers = Number.objects.all()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            body_message = form.cleaned_data.get('body_message')
            for number in all_numbers:
                client.messages.create(
                    to=str(number.phone_number),
                    from_="+12092088123",
                    body=str(body_message),)

            return None
    else:
        form = MessageForm()

    context = {
        'form': form,
        'title': 'SMSuela',
        'all_numbers': all_numbers,
    }
    return render(request, 'home/index.html', context)


def new_number(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            number = form.save(commit=False)
            number.save()
            return HttpResponseRedirect('/numbers')
    else:
        form = NumberForm()

    template = loader.get_template('home/new_number.html')
    context = {
        'form': form,
        'title': 'Agregar número'
    }

    return HttpResponse(template.render(context, request))
