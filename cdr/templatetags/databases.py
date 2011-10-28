from django import template
from django.conf import settings

register = template.Library()

def databases():
    dbs = settings.DATABASES
    return {'databases':dbs}
register.inclusion_tag('cdr/inclusion_tags/databases.html')(databases)
  