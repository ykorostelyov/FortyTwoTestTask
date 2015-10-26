from django.test import TestCase
import os
import subprocess


class TestCommands(TestCase):
    def test_get_models_info(self):
        """
        Test my custom command.
        Using subprocess.Popen, because of "django DeprecationWarning:
        os.popen4 is deprecated. Use the subprocess module." warning
        """
        source = os.getcwd()+'/manage.py get_models_info'
        p = subprocess.Popen([source], stderr=subprocess.STDOUT,
                             stdout=subprocess.PIPE,
                             universal_newlines=True, shell=True)
        p.wait()
        output = [l.strip() for l in p.stdout]
        self.assertIn('RequestInfo', str(output))
        self.assertIn('Mycard', str(output))
        self.assertIn('EventLog', str(output))
