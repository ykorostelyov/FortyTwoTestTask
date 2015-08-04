# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mycard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fName', models.CharField(max_length=100)),
                ('lName', models.CharField(max_length=100)),
                ('bDate', models.DateField()),
                ('eMail', models.EmailField(max_length=254)),
                ('Jabber', models.CharField(max_length=100)),
                ('Skype', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=1024)),
                ('otherContacts', models.CharField(max_length=200)),
            ],
        ),
    ]
