from django.test import TestCase
import os


class TestCommands(TestCase):
    def test_get_models_info(self):
        """
        Test my custom command.
        """
        
        fin, fout = os.popen4('python manage.py get_models_info')
        result = fout.read()
        self.assertIn('apps.hello.models.RequestInfo', result)
        self.assertIn('apps.hello.models.Mycard', result)
        self.assertIn('apps.hello.models.EventLog', result)
