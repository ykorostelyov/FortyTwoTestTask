from django.db.models import get_app, get_models
from django.db.models import loading
from django.core.management.base import BaseCommand
import datetime
import sys


class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Command printed all app models with objects count of each model'

    def handle(self, *args, **options):
        # get full list of apps in settings
        for mod in loading.get_apps():
            # get all apps in [apps] folder
            if 'apps.' in mod.__name__:
                curr_app = mod.__name__
                # get current app name
                app = get_app(str(curr_app)[5:][:-7])
                # get all models of current app
                for model in get_models(app):
                    curr_str = 'MODEL [' + \
                               str(model)[13:][:-2] + \
                               '] have [' + \
                               str(model.objects.all().count()) + \
                               '] object(s)'
                    print curr_str
                    sys.stderr.write('error: '+str(datetime.datetime.now(
                    ))+' '+curr_str+'\n')
