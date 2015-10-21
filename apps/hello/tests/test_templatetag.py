# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client


class TestTemlatetag(TestCase):
    fixtures = ['initial_data.json']

    def test_settings_link_for_current_user(self):
        """
        testing of correctly generating settings link for current user
        """
        # Logging
        c = Client()
        c.login(username="admin", password="admin")
        response = c.get(reverse('home'))
        self.assertContains(response, '/admin/hello/mycard/1/')
