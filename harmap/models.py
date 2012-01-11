import json, socket

from urlparse import urlparse
from django.contrib.gis.db import models
from django.contrib.gis.utils import GeoIP

def create_har(har):
    file_name = har.name
    json_har = json.load(har)
    hosts = dict()
    har = HAR.objects.create(name=file_name)
    for entry in json_har['log']['entries']:
        host = urlparse(entry['request']['url']).hostname
        if host in hosts:
            hosts[host]['time'] += int(entry['time'])
            hosts[host]['asset_count'] += 1
        else: 
            hosts[host] = {
                'url': host,
                'time': int(entry['time']),
                'ip_address': socket.gethostbyname(host),
                'har': har,
                'asset_count': 1,
                }
    for host, kwargs in hosts.items():
        Host.objects.create(**kwargs)

class HAR(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    loaded_from = models.PointField(null=True, blank=True)

    def __unicode__(self):
        return "%s - %s - #%s Hosts" % (self.name, self.created, self.host_set.count())

    @property
    def time(self):
        return sum([host.time for host in self.host_set.all()])

class Host(models.Model):
    url = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=15, null=True, blank=True)
    ip_address_v6 = models.CharField(max_length=19, null=True, blank=True)
    location = models.PointField()
    time = models.IntegerField(null=True, blank=True)
    asset_count = models.IntegerField(null=True, blank=True)
    har = models.ForeignKey(HAR)

    def __unicode__(self):
        return "%s - %s - %s" % (self.url, self.ip_address, self.location.coords)

    def save(self, *args, **kwargs):
        if not self.location:
            self._set_location()
        super(Host, self).save(*args, **kwargs)

    def _set_location(self):
        g = GeoIP()
        self.location = g.geos(self.ip_address)

