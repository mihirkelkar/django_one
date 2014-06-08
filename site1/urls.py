from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from site1.views import hello
from site1.views import time
from site1.views import newtime
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'site1.views.home', name='home'),
    # url(r'^site1/', include('site1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', time),
    url(r'^hello/$', hello),
    #dynamic views. 
    url(r'^(\d{1,2})/$', newtime),
)
