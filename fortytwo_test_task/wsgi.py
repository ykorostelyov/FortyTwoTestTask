"""
WSGI config for fortytwo_test_task project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fortytwo_test_task.settings")
sys.path.insert(0,
                os.path.join(os.path.abspath(os.path.dirname(__file__))
                             , '..'))

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
