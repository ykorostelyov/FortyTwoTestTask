from django.test import TestCase
from .models import Mycard


class TestMycardModel(TestCase):
    Skype_str = "yuriy.torhammer"

    def setUp(self):
        Mycard.objects.create(first_name='Yuriy',
                              last_name='Korostelyov',
                              skype=self.Skype_str,
                              birth_date="1983-01-13",
                              jabber='ykorostelyov@khavr.com'
                              )

    def test_person(self):
        """Testing of My card creatig"""
        mycard = Mycard.objects.get(id='1')
        self.assertEqual(mycard.skype, self.Skype_str)
        self.assertEqual(mycard.jabber, 'ykorostelyov@khavr.com')
