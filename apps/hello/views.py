from django.shortcuts import render_to_response
from .models import Mycard
import logging
from django.shortcuts import get_object_or_404


log = logging.getLogger('apps')


# index
def index(request):
    # Check for Model is present
    mycard = get_object_or_404(Mycard, id=1)
    log.info('Getting data of model for homepage')
    log.debug('rec for ' + mycard.first_name +
              ' ' + mycard.last_name + ' person')
    log.debug('Displayng russian characters. bio = ' + mycard.bio)
    first_result = Mycard.objects.order_by('id')[0]
    return render_to_response("hello/index.html",
                              {'first_result': first_result})
