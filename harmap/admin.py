from django.contrib.gis import admin
from models import Host, HAR

admin.site.register(Host, admin.GeoModelAdmin)
admin.site.register(HAR, admin.GeoModelAdmin)
