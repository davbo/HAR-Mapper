# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'HAR'
        db.create_table('harmap_har', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('loaded_from', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
        ))
        db.send_create_signal('harmap', ['HAR'])

        # Adding model 'Host'
        db.create_table('harmap_host', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ip_address', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('ip_address_v6', self.gf('django.db.models.fields.CharField')(max_length=19, null=True, blank=True)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('har', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['harmap.HAR'])),
        ))
        db.send_create_signal('harmap', ['Host'])


    def backwards(self, orm):
        
        # Deleting model 'HAR'
        db.delete_table('harmap_har')

        # Deleting model 'Host'
        db.delete_table('harmap_host')


    models = {
        'harmap.har': {
            'Meta': {'object_name': 'HAR'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loaded_from': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'harmap.host': {
            'Meta': {'object_name': 'Host'},
            'har': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['harmap.HAR']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'ip_address_v6': ('django.db.models.fields.CharField', [], {'max_length': '19', 'null': 'True', 'blank': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['harmap']
