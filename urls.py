from django.conf.urls.defaults import *
from django.contrib.gis import admin
from harmap import views

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'hars/', 'harmap.views.har_list'),
    (r'har/(?P<id>\d+)/$', 'harmap.views.har_map'),
    )
