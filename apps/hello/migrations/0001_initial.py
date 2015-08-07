# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mycard'
        db.create_table(u'Mydata_mycard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fName', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('lName', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('bDate', self.gf('django.db.models.fields.DateField')()),
            ('eMail', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('Jabber', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Skype', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('bio', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('otherContacts', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'hello', ['Mycard'])


    def backwards(self, orm):
        # Deleting model 'Mycard'
        db.delete_table(u'Mydata_mycard')


    models = {
        u'hello.mycard': {
            'Jabber': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Mycard'},
            'Skype': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'bDate': ('django.db.models.fields.DateField', [], {}),
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'eMail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'otherContacts': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['hello']