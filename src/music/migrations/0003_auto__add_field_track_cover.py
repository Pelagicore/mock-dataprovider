# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding field 'Track.cover'
        db.add_column('music_track', 'cover',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Track.cover'
        db.delete_column('music_track', 'cover')


    models = {
        'music.track': {
            'Meta': {'object_name': 'Track'},
            'album': ('django.db.models.fields.CharField', [], {'default': "'No Album'", 'max_length': '200'}),
            'artist': ('django.db.models.fields.CharField', [], {'default': "'No Artist'", 'max_length': '200'}),
            'cover': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'No Title'", 'max_length': '200'}),
            'track': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8'})
        }
    }

    complete_apps = ['music']