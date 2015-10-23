# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from apps.hello.models import Mycard, EventLog


class TestSignals(TestCase):
    def test_signals(self):
        """
        testing of signals for existing models (on create, on change,
        on delete)
        """

        # creating
        EventLog.objects.all().delete()
        c = Client()
        c.get(reverse('home'))
        event_log_count = EventLog.objects.filter(
            event="Created").count()

        self.assertEqual(event_log_count, 1)

        # changing
        EventLog.objects.all().delete()
        for card in Mycard.objects.filter(
                jabber="ykorostelyov@khavr.com").all():
            card.save()
        event_log_count = EventLog.objects.count()
        self.assertEqual(event_log_count, 2)

        # deleting
        EventLog.objects.all().delete()
        Mycard.objects.all().delete()
        event_log_count = EventLog.objects.filter(
            event="Deleted").count()
        self.assertEqual(event_log_count, 1)
