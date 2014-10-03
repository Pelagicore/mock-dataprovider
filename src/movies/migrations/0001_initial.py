# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table('movies_movie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cover', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
        ))
        db.send_create_signal('movies', ['Movie'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table('movies_movie')


    models = {
        'movies.movie': {
            'Meta': {'object_name': 'Movie'},
            'cover': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'})
        }
    }

    complete_apps = ['movies']