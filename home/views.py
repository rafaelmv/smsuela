from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NumberForm
from .models import Number

from django.views.generic import ListView


class NumberList(ListView):
    model = Number
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(NumberList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'Números'
        return context


def index(request):
    context = {
        'title': 'SMSuela'
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
