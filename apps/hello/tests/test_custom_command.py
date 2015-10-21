import os
from django.test import TestCase


class TestCommand(TestCase):

    def test_command(self):
        """
        testing of command output
        """
        console = os.popen('python manage.py get_models_info')
        self.assertIn('hello.models.RequestInfo', console.read())
        console = os.popen('python manage.py get_models_info')
        self.assertIn('hello.models.Mycard', console.read())
