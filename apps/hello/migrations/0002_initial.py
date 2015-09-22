# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'RequestInfo.fromIP'
        db.delete_column(u'hello_requestinfo', 'fromIP')

        # Deleting field 'RequestInfo.isViewed'
        db.delete_column(u'hello_requestinfo', 'isViewed')

        # Adding field 'RequestInfo.host'
        db.add_column(u'hello_requestinfo', 'host',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1024),
                      keep_default=False)

        # Adding field 'RequestInfo.remote_addr'
        db.add_column(u'hello_requestinfo', 'remote_addr',
                      self.gf('django.db.models.fields.GenericIPAddressField')(default=1, max_length=39),
                      keep_default=False)

        # Adding field 'RequestInfo.is_viewed'
        db.add_column(u'hello_requestinfo', 'is_viewed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'RequestInfo.is_ajax'
        db.add_column(u'hello_requestinfo', 'is_ajax',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'RequestInfo.uri'
        db.add_column(u'hello_requestinfo', 'uri',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1024),
                      keep_default=False)

        # Adding field 'RequestInfo.status_code'
        db.add_column(u'hello_requestinfo', 'status_code',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=30),
                      keep_default=False)

        # Adding field 'RequestInfo.user_agent'
        db.add_column(u'hello_requestinfo', 'user_agent',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1024),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'RequestInfo.fromIP'
        db.add_column(u'hello_requestinfo', 'fromIP',
                      self.gf('django.db.models.fields.GenericIPAddressField')(default=1, max_length=39),
                      keep_default=False)

        # Adding field 'RequestInfo.isViewed'
        db.add_column(u'hello_requestinfo', 'isViewed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'RequestInfo.host'
        db.delete_column(u'hello_requestinfo', 'host')

        # Deleting field 'RequestInfo.remote_addr'
        db.delete_column(u'hello_requestinfo', 'remote_addr')

        # Deleting field 'RequestInfo.is_viewed'
        db.delete_column(u'hello_requestinfo', 'is_viewed')

        # Deleting field 'RequestInfo.is_ajax'
        db.delete_column(u'hello_requestinfo', 'is_ajax')

        # Deleting field 'RequestInfo.uri'
        db.delete_column(u'hello_requestinfo', 'uri')

        # Deleting field 'RequestInfo.status_code'
        db.delete_column(u'hello_requestinfo', 'status_code')

        # Deleting field 'RequestInfo.user_agent'
        db.delete_column(u'hello_requestinfo', 'user_agent')


    models = {
        u'hello.mycard': {
            'Meta': {'object_name': 'Mycard'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hello.requestinfo': {
            'Meta': {'object_name': 'RequestInfo'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ajax': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_viewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'remote_addr': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'status_code': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['hello']