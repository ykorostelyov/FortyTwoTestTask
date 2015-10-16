# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RequestInfo.priority'
        db.add_column(u'hello_requestinfo', 'priority',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RequestInfo.priority'
        db.delete_column(u'hello_requestinfo', 'priority')


    models = {
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
            'priority': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '2'}),
            'remote_addr': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'status_code': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['hello']