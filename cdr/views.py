from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from cdr.models import Cdr
from datetime import date, datetime, timedelta
from cdr.forms import CdrSearchForm

#@staff_member_required
def home(request):

    if not request.GET.has_key('csrfmiddlewaretoken'):
        form = CdrSearchForm()
        registros = Cdr.objects.filter().using(request.database)
    else:
        form = CdrSearchForm(request.GET)
        if form.is_valid():
            date_from = form.cleaned_data.get('calldate_from')
            date_to = form.cleaned_data.get('calldate_to')
            if date_to:
                date_to = date_to + timedelta(days=1)

            registros = Cdr.objects.all().using(request.database)

            if date_from:
                registros = Cdr.objects.filter(calldate__gte=date_from).using(request.database)
            if date_to:
                registros = Cdr.objects.filter(calldate__lte=date_to).using(request.database)

            disposition = form.cleaned_data.get('disposition', 'ALL')
            if disposition != 'ALL':
                registros = registros.filter(disposition=disposition).using(request.database)
            
        
    return render_to_response("cdr/index.html",
                                {'registros':registros, 'form':form},
                                context_instance=RequestContext(request))

#@staff_member_required
def set_db(request, database):
    request.session['DB'] = database
    return HttpResponseRedirect(reverse('home'))