# coding=utf-8

from django.shortcuts import (
    render,
    get_object_or_404
)
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


from .forms import NumberForm, MessageForm
from .models import Number, Message

from twilio.rest import Client


client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)


def home_page(request):
    last_ten_messages = Message.objects.all().order_by('created_at')[:10]
    context = {
        'last_ten_messages': last_ten_messages
    }
    return render(request, 'home/index.html', context)


class NumberList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Number

    def get_context_data(self, **kwargs):
        context = super(NumberList, self).get_context_data(**kwargs)
        return context


@login_required(login_url='/login')
def new_message(request):

    all_numbers = Number.objects.all()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            text_message = form.save(commit=False)
            text_message.save()

            body_message = form.cleaned_data['text_message']

            for number in all_numbers:

                client.messages.create(
                    to=str(number.phone_number),
                    from_="+12092088123",
                    body=str(body_message))

            messages.success(request, 'Mensaje enviado.')
            return HttpResponseRedirect('/message/new/')
    else:
        form = MessageForm()

    context = {
        'form': form,
        'all_numbers': all_numbers,
    }
    return render(request, 'home/new_message.html', context)


@login_required(login_url='/login')
def new_number(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            number = form.save(commit=False)
            number.save()
            messages.success(request, 'Número guardado.')
            return HttpResponseRedirect('/numbers')
    else:
        form = NumberForm()

    template = loader.get_template('home/new_number.html')
    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))
