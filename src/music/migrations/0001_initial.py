# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Track'
        db.create_table('music_track', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='No Title', max_length=200)),
            ('album', self.gf('django.db.models.fields.CharField')(default='No Album', max_length=200)),
            ('artist', self.gf('django.db.models.fields.CharField')(default='No Artist', max_length=200)),
            ('track', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('source', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
        ))
        db.send_create_signal('music', ['Track'])


    def backwards(self, orm):
        # Deleting model 'Track'
        db.delete_table('music_track')


    models = {
        'music.track': {
            'Meta': {'object_name': 'Track'},
            'album': ('django.db.models.fields.CharField', [], {'default': "'No Album'", 'max_length': '200'}),
            'artist': ('django.db.models.fields.CharField', [], {'default': "'No Artist'", 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': (
            'django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'No Title'", 'max_length': '200'}),
            'track': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        }
    }

    complete_apps = ['music']