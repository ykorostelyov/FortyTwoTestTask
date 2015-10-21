# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from django.contrib.admin.models import LogEntry
from apps.hello.models import Mycard


class TestSignals(TestCase):
    def test_signals(self):
        """
        testing of signals for existing models (on create, on change,
        on delete)
        """

        # creating
        LogEntry.objects.all().delete()
        c = Client()
        c.get(reverse('home'))
        log_entry_count = LogEntry.objects.filter(
            change_message="created object").count()

        self.assertEqual(log_entry_count, 1)
        # changing
        LogEntry.objects.all().delete()
        for card in Mycard.objects.filter(
                jabber="ykorostelyov@khavr.com").all():
            card.save()
        log_entry_count = LogEntry.objects.count()
        self.assertEqual(log_entry_count, 2)
        # deleting
        LogEntry.objects.all().delete()
        Mycard.objects.all().delete()
        log_entry_count = LogEntry.objects.filter(
            change_message="deleting object").count()
        self.assertEqual(log_entry_count, 1)
