from django.shortcuts import render_to_response
from .models import Mycard
from django.http import Http404
import logging


log = logging.getLogger('apps')


# index
def index(request):
    try:
        mycard = Mycard.objects.get(id=1)
    except Mycard.DoesNotExist:
        raise Http404

    log.info('Getting data of model for homepage')
    log.debug('record for ' + mycard.first_name +
              ' ' + mycard.last_name + ' person')
    log.debug('Displayng Unicode characters. bio = ' + mycard.bio)

    first_result = Mycard.objects.order_by('id')[0]
    return render_to_response("hello/index.html",
                              {'first_result': first_result})
