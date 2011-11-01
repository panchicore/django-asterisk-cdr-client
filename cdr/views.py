from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from cdr.models import Cdr
from datetime import date, datetime
from cdr.forms import CdrSearchForm

def home(request):

    if not request.GET.has_key('csrfmiddlewaretoken'):
        form = CdrSearchForm()
        registros = Cdr.objects.filter(calldate__startswith=date.today()).using(request.database)
    else:
        form = CdrSearchForm(request.GET)
        if form.is_valid():
            date_from = form.cleaned_data.get('calldate_from')
            date_to = form.cleaned_data.get('calldate_to')
            registros = Cdr.objects.filter(calldate__gte=date_from, calldate__lte=date_to).using(request.database)
            
        
    return render_to_response("cdr/index.html",
                                {'registros':registros, 'form':form},
                                context_instance=RequestContext(request))


def set_db(request, database):
    request.session['DB'] = database
    return HttpResponseRedirect(reverse('home'))