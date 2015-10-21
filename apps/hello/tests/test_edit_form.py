# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from apps.hello.models import Mycard
from django.template.defaultfilters import escape, date


class TestEditForm(TestCase):
    fixtures = ['initial_data.json']

    def test_login_page(self):
        """
        Login page checking
        """
        c = Client()
        response = c.get('/accounts/login/')
        self.assertEquals(response.status_code, 200)

    def test_edit_login_required(self):
        """
        Checking of login required in edit page
        """
        # Goto edit not logged on
        response = self.client.get(reverse('edit'))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn("edit-form", response)

        # Logging
        c = Client()
        c.login(username="admin", password="admin")
        response = c.get(reverse('edit'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "edit-form")
        # Is correct template used
        self.assertTemplateUsed(response, 'hello/edit.html')

    def test_edit_post_method(self):
        """
        Testing edit view - rendering posted data, saving data into db
        """
        # truncate db_table
        Mycard.objects.all().delete()

        c = Client()
        # filling dict
        my_data_dict = dict()
        my_data_dict['first_name'] = 'Yuriy4'
        my_data_dict['last_name'] = 'Korostelyov4'
        my_data_dict['birth_date'] = '1983-01-13'
        my_data_dict['email'] = 'ykorostelyov4@gmail.com'
        my_data_dict['jabber'] = 'ykorostelyov4@gmail.com'
        my_data_dict['skype'] = 'yuriy.torhammer4'
        my_data_dict['bio'] = "Some boio 4"
        my_data_dict['other_contacts'] = "4"

        # 0 records in mycard table
        self.assertEqual(Mycard.objects.count(), 0)
        c.login(username='admin', password='admin')

        # posting data
        response = c.post('/edit/', my_data_dict, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Mycard.objects.count(), 1)

        # Rendered content
        self.assertContains(response, my_data_dict['first_name'])
        self.assertContains(response, my_data_dict['last_name'])
        self.assertContains(response, date(my_data_dict['birth_date']))
        self.assertContains(response, my_data_dict['email'])
        self.assertContains(response, my_data_dict['jabber'])
        self.assertContains(response, my_data_dict['skype'])
        self.assertContains(response, escape(my_data_dict['bio']))
        self.assertContains(response, my_data_dict['other_contacts'])

        # recorded data
        mycard = Mycard.objects.first()
        self.assertEqual(mycard.first_name, my_data_dict['first_name'])
        self.assertEqual(mycard.last_name, my_data_dict['last_name'])
        self.assertEqual(mycard.email, my_data_dict['email'])
        self.assertEqual(mycard.jabber, my_data_dict['jabber'])
        self.assertEqual(mycard.skype, my_data_dict['skype'])
        self.assertEqual(mycard.bio, escape(my_data_dict['bio']))
        self.assertEqual(mycard.other_contacts, my_data_dict['other_contacts'])
