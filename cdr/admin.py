from django.http import HttpResponse
from django.template.loader import render_to_string
import time

__author__ = 'panchicore'

from cdr.models import Cdr, Rate
from django.contrib import admin

def export_to_xls(modeladmin, request, queryset):
    model = modeladmin.model
    params = request.GET.items()
    dict = {}

    print params

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
        

    res = render_to_string("export/xls.html", {'registros':objects, 'duracion_total':duracion_total, 'gran_total':gran_total})
    return HttpResponse(res)

export_to_xls.short_description = "Exportar a XLS"

class CdrAdmin(admin.ModelAdmin):
    list_display = ('uniqueid', 'calldate', 'duration', 'tiempo_facturado', 'disposition')
    list_filter = ('disposition',)
    search_fields = ('uniqueid',)
    date_hierarchy = 'calldate'
    actions = [export_to_xls]


admin.site.register(Cdr, CdrAdmin)
admin.site.register(Rate)