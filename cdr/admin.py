from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
import time

__author__ = 'panchicore'

from cdr.models import Cdr, Rate
from django.contrib import admin

def export_to_xls(modeladmin, request, queryset):
    model = modeladmin.model
    params = request.GET.items()
    dict = {}

    #if params[0].has_key('o'): params.pop('o')
    #if params[0].has_key('ot'): params.pop('ot')

    for p in params:
        key = '%s' % str(p[0])
        val = str(p[1])
        dict[key] = val

    objects = model.objects.filter(**dict)

    duracion_total = 0
    gran_total = 0

    for o in objects:
        duracion_total += o.billsec

    duracion_total = duracion_total / 60
    rate = Rate.objects.get()
    gran_total = duracion_total * rate.value

    response = render_to_response("export/xls.html", {'registros':objects, 'duracion_total':duracion_total, 'gran_total':gran_total})
    filename = "invoice.xls"
    response['Content-Disposition'] = 'attachment; filename='+filename

    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response

export_to_xls.short_description = "Exportar a XLS"

class CdrAdmin(admin.ModelAdmin):
    list_display = ('uniqueid', 'calldate', 'duration', 'tiempo_facturado', 'disposition')
    list_filter = ('disposition',)
    search_fields = ('uniqueid',)
    date_hierarchy = 'calldate'
    actions = [export_to_xls]


admin.site.register(Cdr, CdrAdmin)
admin.site.register(Rate)