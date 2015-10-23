from django.db.models import get_apps, get_models
from django.core.management.base import BaseCommand
import datetime
import sys


class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Command print all app models with objects count of each model'

    def handle(self, *args, **options):
        for app in get_apps():
            for model in get_models(app):
                curr_str = str(model)+' have ' \
                                      ''+'['+str(model.objects.
                                                 all().count())+'] ' \
                                                                'object(s)'
                print curr_str
                sys.stderr.write('error:'
                                 ' '+str(datetime.datetime.now()) +
                                 ' '+curr_str+'\n')
