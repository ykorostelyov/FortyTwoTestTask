# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'RequestInfo.priority'
        db.delete_column(u'hello_requestinfo', 'priority')

        # Adding field 'RequestInfo.priority_num'
        db.add_column(u'hello_requestinfo', 'priority_num',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'RequestInfo.priority'
        db.add_column(u'hello_requestinfo', 'priority',
                      self.gf('django.db.models.fields.IntegerField')(default=1, max_length=3),
                      keep_default=False)

        # Deleting field 'RequestInfo.priority_num'
        db.delete_column(u'hello_requestinfo', 'priority_num')


    models = {
        u'hello.eventlog': {
            'Meta': {'object_name': 'EventLog'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '150'})
        },
        u'hello.mycard': {
            'Meta': {'object_name': 'Mycard'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'priority_num': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'remote_addr': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'status_code': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['hello']