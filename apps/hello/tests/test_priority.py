# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import RequestInfo


class TestPriority(TestCase):

    def test_get_post_priority(self):
        """
        Testing of priority sorting
        """
        RequestInfo.objects.all().delete()

        self.client.get(reverse('home'))
        first_id = RequestInfo.objects.last().id

        response = self.client.get(reverse('requests'))
        for i in range(11):
            self.client.get(reverse('home'))

        # having list with only 1 priority
        self.assertEqual(response.context['requests_list'][0].priority_num, 0)

        # changing priority in first record
        RequestInfo.objects.filter(id=first_id).update(priority_num=3)
        response = self.client.get(reverse('requests'))

        # first record on the top of the list
        self.assertEqual(response.context['requests_list'][0].priority_num, 3)
        self.assertContains(response, 'priority-3', 0)
