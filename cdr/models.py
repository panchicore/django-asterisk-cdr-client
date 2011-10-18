from django.db import models
import time

DISPOSITION = (
    ('FAILED','FAILED'),
    ('ANSWERED','ANSWERED'),
    ('NO ANSWER','NO ANSWER'),
    ('BUSY','BUSY'),
)

class Cdr(models.Model):
    calldate = models.DateTimeField()
    clid = models.CharField(max_length=240)
    src = models.CharField(max_length=240)
    dst = models.CharField(max_length=240)
    dcontext = models.CharField(max_length=240)
    channel = models.CharField(max_length=240)
    dstchannel = models.CharField(max_length=240)
    lastapp = models.CharField(max_length=240)
    lastdata = models.CharField(max_length=240)
    duration = models.IntegerField()
    billsec = models.IntegerField()
    disposition = models.CharField(max_length=135)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=60)
    uniqueid = models.CharField(max_length=96, primary_key=True)
    userfield = models.CharField(max_length=765)
    
    class Meta:
        db_table = u'cdr'
        verbose_name = 'registro de llamada'
        verbose_name_plural = 'registros de llamadas'

    def __unicode__(self):
        return 'callid: %s "%s" (%i)' % (self.uniqueid, self.disposition, self.duration)

    @property
    def duration_time(self):
        return time.strftime('%H:%M:%S', time.gmtime(self.duration))

