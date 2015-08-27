# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Mycard
import datetime


class TestMycardModel(TestCase):

    def test__is_init_data_correct(self):
        """Testing of init data accuracy"""
        # Is All properties included
        mycard = Mycard.objects.get(id=1)
        self.assertIsNotNone(mycard)
        self.assertIn('first_name', mycard.__dict__)
        self.assertIn('last_name', mycard.__dict__)
        self.assertIn('skype', mycard.__dict__)
        self.assertIn('birth_date', mycard.__dict__)
        self.assertIn('jabber', mycard.__dict__)
        self.assertIn('bio', mycard.__dict__)
        self.assertIn('other_contacts', mycard.__dict__)
        # Is data correct
        self.assertEqual(mycard.jabber, 'ykorostelyov@khavr.com')
        self.assertEqual(mycard.first_name+' '+mycard.last_name,
                         'Yuriy Korostelyov')
        self.assertNotEqual(len(mycard.bio), 0)
        self.assertNotEqual(len(mycard.other_contacts), 0)
        self.assertNotEqual(mycard.birth_date, datetime.date.today())

    def test_view__unicode_characters(self):
        """Displaying of Unicode characters"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        # Unicode testing (bio, other contacts)
        self.assertContains(response, u'Биография')
        self.assertContains(response, u'Другие')

    def test_view__raising_404_when_no_data(self):
        """raising 404 when no_data for view"""
        total_records_count = Mycard.objects.filter().count()
        with self.assertRaises(Http404):
            get_object_or_404(Mycard, pk=total_records_count+1)

    def test_view__only_one_record_from_db(self):
        """Only one record from db showing in view"""
        Mycard.objects.create(first_name=u'Имя2',
                              last_name=u'Фамилия2',
                              bio=u'Био2',
                              email=u'ykorostelyov@gmail.com',
                              jabber=u'ykorostelyov@khavr.com',
                              skype=u'yuriy.torhammer',
                              birth_date=u'1983-01-13',
                              other_contacts=u'Другие контакты2')

        total_records_count = Mycard.objects.count()
        self.assertGreaterEqual(total_records_count, 2)

        response = self.client.get(reverse('home'))
        self.assertNotEqual(response, u'Имя2')
