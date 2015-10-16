# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Mycard.lName'
        db.delete_column(u'hello_mycard', 'lName')

        # Deleting field 'Mycard.otherContacts'
        db.delete_column(u'hello_mycard', 'otherContacts')

        # Deleting field 'Mycard.fName'
        db.delete_column(u'hello_mycard', 'fName')

        # Deleting field 'Mycard.bDate'
        db.delete_column(u'hello_mycard', 'bDate')

        # Deleting field 'Mycard.Skype'
        db.delete_column(u'hello_mycard', 'Skype')

        # Deleting field 'Mycard.Jabber'
        db.delete_column(u'hello_mycard', 'Jabber')

        # Deleting field 'Mycard.eMail'
        db.delete_column(u'hello_mycard', 'eMail')

        # Adding field 'Mycard.first_name'
        db.add_column(u'hello_mycard', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Mycard.last_name'
        db.add_column(u'hello_mycard', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Mycard.birth_date'
        db.add_column(u'hello_mycard', 'birth_date',
                      self.gf('django.db.models.fields.DateField')(default="1983-01-13"),
                      keep_default=True)

        # Adding field 'Mycard.email'
        db.add_column(u'hello_mycard', 'email',
                      self.gf('django.db.models.fields.EmailField')(default=1, max_length=75),
                      keep_default=False)

        # Adding field 'Mycard.jabber'
        db.add_column(u'hello_mycard', 'jabber',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Mycard.skype'
        db.add_column(u'hello_mycard', 'skype',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Mycard.other_contacts'
        db.add_column(u'hello_mycard', 'other_contacts',
                      self.gf('django.db.models.fields.TextField')(default=1),
                      keep_default=False)


        # Changing field 'Mycard.bio'
        db.alter_column(u'hello_mycard', 'bio', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Adding field 'Mycard.lName'
        db.add_column(u'hello_mycard', 'lName',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Mycard.otherContacts'
        db.add_column(u'hello_mycard', 'otherContacts',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)

        # Adding field 'Mycard.fName'
        db.add_column(u'hello_mycard', 'fName',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Mycard.bDate'
        db.add_column(u'hello_mycard', 'bDate',
                      self.gf('django.db.models.fields.DateField')(default=1),
                      keep_default=False)

        # Adding field 'Mycard.Skype'
        db.add_column(u'hello_mycard', 'Skype',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Mycard.Jabber'
        db.add_column(u'hello_mycard', 'Jabber',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Mycard.eMail'
        db.add_column(u'hello_mycard', 'eMail',
                      self.gf('django.db.models.fields.EmailField')(default=1, max_length=75),
                      keep_default=False)

        # Deleting field 'Mycard.first_name'
        db.delete_column(u'hello_mycard', 'first_name')

        # Deleting field 'Mycard.last_name'
        db.delete_column(u'hello_mycard', 'last_name')

        # Deleting field 'Mycard.birth_date'
        db.delete_column(u'hello_mycard', 'birth_date')

        # Deleting field 'Mycard.email'
        db.delete_column(u'hello_mycard', 'email')

        # Deleting field 'Mycard.jabber'
        db.delete_column(u'hello_mycard', 'jabber')

        # Deleting field 'Mycard.skype'
        db.delete_column(u'hello_mycard', 'skype')

        # Deleting field 'Mycard.other_contacts'
        db.delete_column(u'hello_mycard', 'other_contacts')


        # Changing field 'Mycard.bio'
        db.alter_column(u'hello_mycard', 'bio', self.gf('django.db.models.fields.CharField')(max_length=1024))

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
        }
    }

    complete_apps = ['hello']