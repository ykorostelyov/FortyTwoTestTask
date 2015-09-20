# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Mycard
from .models import RequestInfo
import datetime
from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


class TestMycardModel(TestCase):

    def test__is_init_data_correct(self):
        """
        Testing of init data accuracy
        """
        # Is All properties included
        mycard = Mycard.objects.first()
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
        """
        Displaying of Unicode characters
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        # Unicode testing (bio, other contacts)
        self.assertContains(response, u'Биография')
        self.assertContains(response, u'Другие')

    def test_view__raising_404_when_no_data(self):
        """
        raising 404 when no_data for view
        """
        Mycard.objects.all().delete()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 404)

    def test_view__only_one_record_from_db(self):
        """
        Only one record from db showing in view
        """
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

    def test_view__using_rendering_data_from_db(self):
        """
        Using of rendering data, not static
        """
        # Deleting all data to check response
        Mycard.objects.all().delete()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 404)
        # Creating DB record for rendering
        mycard = Mycard.objects.create(first_name='Имя3',
                                       last_name='Фамилия3',
                                       bio=u'Био3',
                                       email=u'ykorostelyov@gmail.com',
                                       jabber=u'ykorostelyov@khavr.com',
                                       skype=u'yuriy.torhammer',
                                       birth_date=u'1983-01-13',
                                       other_contacts=u'Другие контакты3')

        # calling home view with rendered data
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        # Checking of rendered data
        self.assertEqual(mycard.__unicode__(),
                         str(response.context['first_result']))


class SelTest(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.PhantomJS()
        super(SelTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SelTest, self).tearDown()


class TestLiveRequests(SelTest):

    def test_only_10_requests(self):
        """
        Show last 10 http requests that are stored by middleware
        """
        RequestInfo.objects.all().delete()
        # calling home 12 times
        for i in range(12):
            self.client.get(reverse('home'))

        # more than 10 requests in db
        self.assertTrue(RequestInfo.objects.all().count() > 10)

        driver = webdriver.PhantomJS()
        driver.get('%s%s' % (self.live_server_url, '/requests/'))
        # only 10 requests rendered
        self.assertEqual(len(driver.find_elements_by_class_name(
            'request_unreaded')), 10)

        try:
            WebDriverWait(self.selenium, 10)\
                .until(expected_conditions
                       .presence_of_element_located((By.TAG_NAME,
                                                    "td")))
        except TimeoutException:
            pass

        driver.quit()

    def test_title_count(self):
        """
        If there are N new requests, page title should start with (N)
        """
        RequestInfo.objects.all().delete()
        # Must have 3 new requests
        for i in range(2):
            self.client.get(reverse('requests'))
        driver = webdriver.PhantomJS()
        driver.get('%s%s' % (self.live_server_url, '/requests/'))
        self.assertEquals('(3) New requests', driver.title)
        # Must have 1 new requests
        RequestInfo.objects.all().delete()
        driver.get('%s%s' % (self.live_server_url, '/requests/'))
        self.assertEquals('(1) New requests', driver.title)

        driver.quit()

    def test_render(self):
        """
        Checking of rendered data
        """
        # Response ok
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.status_code, 200)
        # Using correct template
        self.assertTemplateUsed(response, 'hello/requests.html')
