from django.conf.urls.defaults import patterns, include, url

from settings import MEDIA_ROOT
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
    url(r'^$', 'cdr.views.home', name='home'),
    url(r'^db/(?P<database>\w+)/$', 'cdr.views.set_db', name='set_db'),
    # url(r'^asteriskcdrdb/', include('asteriskcdrdb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
