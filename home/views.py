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

def index(request):
    return render(request, 'home/index.html')

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
        'form': form
    }

    return HttpResponse(template.render(context, request))
