# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import RequestInfo


class TestRequests(TestCase):

    def test_only_10_requests_and_title_count(self):
        """
        - Showing only 10 http requests that are stored by middleware
        - Current new records count
        """
        RequestInfo.objects.all().delete()
        # more than 10 requests in db
        for i in range(11):
            self.client.get(reverse('home'))
        self.assertTrue(RequestInfo.objects.all().count() > 10)
        response = self.client.get(reverse('requests'))

        # only 10 requests rendered
        self.assertEqual(len(response.context['requests_list']), 10)

        # new records count
        RequestInfo.objects.all().delete()
        for i in range(5):
            self.client.get(reverse('home'))
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.context['new_requests_cnt'], 5)

    def test_render(self):
        """
        Checking of rendered data
        """
        # Response ok
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.status_code, 200)
        # Using correct template
        self.assertTemplateUsed(response, 'hello/requests.html')
