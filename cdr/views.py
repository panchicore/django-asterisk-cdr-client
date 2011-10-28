from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from cdr.models import Cdr

def home(request):
    registros = Cdr.objects.all().using(request.database)[0:10]
    return render_to_response("cdr/index.html",
                                {'registros':registros},
                                context_instance=RequestContext(request))


def set_db(request, database):
    request.session['DB'] = database
    return HttpResponseRedirect(reverse('home'))