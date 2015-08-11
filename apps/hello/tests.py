# -*- coding: utf-8 -*-
from django.test import TestCase
from .models import Mycard
import datetime


class TestMycardModel(TestCase):
    Skype_str = "yuriy.torhammer"

    def test_is_mycard_not_clean(self):
        """Testing init data"""
        mycard = Mycard.objects.get(id=1)
        # Is mycard not clean
        self.assertIsNotNone(mycard)

    def test_is_init_data_correct(self):
        """Testing correcting of init data"""
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
        self.assertEqual(mycard.skype, self.Skype_str)
        self.assertEqual(mycard.jabber, 'ykorostelyov@khavr.com')
        self.assertEqual(mycard.first_name+' '+mycard.last_name,
                         'Yuriy Korostelyov')
        self.assertNotEqual(len(mycard.bio), 0)
        self.assertNotEqual(len(mycard.other_contacts), 0)
        self.assertNotEqual(mycard.birth_date, datetime.date.today())

    def test_is_db_have_single_record(self):
        """Testing db on showing only single record"""
        mycard = Mycard.objects.filter(id=1).count()
        # Is received some data
        self.assertNotEqual(mycard, 0)
        # Is received single record
        self.assertEqual(mycard, 1)

    def test_is_data_model_presented_in_db(self):
        """Testing of site structure"""
        # Getting default page
        response = self.client.get('')
        # Is current response valid
        self.assertEqual(response.status_code, 200)
        # Is used template correct
        self.assertTemplateUsed(response, 'hello/index.html')
        # Getting invalid page
        response = self.client.get('invalid')
        # Is current response invalid
        self.assertEqual(response.status_code, 404)
