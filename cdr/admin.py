__author__ = 'panchicore'

from cdr.models import Cdr
from django.contrib import admin

class CdrAdmin(admin.ModelAdmin):
    list_display = ('uniqueid', 'calldate', 'duration', 'duration_time', 'disposition')
    list_filter = ('disposition',)
    search_fields = ('uniqueid',)
    date_hierarchy = 'calldate'


admin.site.register(Cdr, CdrAdmin)