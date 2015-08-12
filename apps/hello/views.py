from django.test import TestCase
from .models import Mycard


class TestMycardModel(TestCase):
    Skype_str = "yuriy.torhammer"

    def setUp(self):
        Mycard.objects.create(fName='Yuriy',
                              lName='Korostelyov',
                              Skype=self.Skype_str,
                              bDate="1983-01-13",
                              Jabber='ykorostelyov@khavr.com'
                              )

    def test_person(self):
        """Testing of My card creatig"""
        mycard = Mycard.objects.get(id='1')
        self.assertEqual(mycard.Skype, self.Skype_str)
        self.assertEqual(mycard.Jabber, 'ykorostelyov@khavr.com')
