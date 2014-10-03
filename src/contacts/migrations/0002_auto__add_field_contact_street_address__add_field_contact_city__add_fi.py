# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Contact.street_address'
        db.add_column('contacts_contact', 'street_address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Contact.city'
        db.add_column('contacts_contact', 'city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Contact.zip_code'
        db.add_column('contacts_contact', 'zip_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=16, blank=True),
                      keep_default=False)

        # Adding field 'Contact.country'
        db.add_column('contacts_contact', 'country',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Contact.email_address'
        db.add_column('contacts_contact', 'email_address',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Contact.street_address'
        db.delete_column('contacts_contact', 'street_address')

        # Deleting field 'Contact.city'
        db.delete_column('contacts_contact', 'city')

        # Deleting field 'Contact.zip_code'
        db.delete_column('contacts_contact', 'zip_code')

        # Deleting field 'Contact.country'
        db.delete_column('contacts_contact', 'country')

        # Deleting field 'Contact.email_address'
        db.delete_column('contacts_contact', 'email_address')


    models = {
        'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'})
        }
    }

    complete_apps = ['contacts']