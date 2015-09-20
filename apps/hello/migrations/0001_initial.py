# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RequestInfo'
        db.create_table(u'hello_requestinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('remote_addr', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('is_viewed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_ajax', self.gf('django.db.models.fields.BooleanField')(
                default=False)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('status_code', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('user_agent', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'hello', ['RequestInfo'])


    def backwards(self, orm):
        # Deleting model 'Mycard'
        db.delete_table(u'hello_mycard')

        # Deleting model 'RequestInfo'
        db.delete_table(u'hello_requestinfo')


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
            'is_viewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_ajax': ('django.db.models.fields.BooleanField', [],
                     {'default': 'False'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'remote_addr': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'status_code': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['hello']