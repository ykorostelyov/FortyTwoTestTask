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
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('email', self.gf('django.db.models.fields.emailField')(max_length=75)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('bio', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('other_contacts', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'hello', ['Mycard'])


    def backwards(self, orm):
        # Deleting model 'Mycard'
        db.delete_table(u'Mydata_mycard')


    models = {
        u'hello.mycard': {
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Mycard'},
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'email': ('django.db.models.fields.emailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'other_contacts': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['hello']