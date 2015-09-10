from django.shortcuts import render_to_response
from .models import Mycard
import logging
from django.http import Http404


log = logging.getLogger('apps')


# index
def index(request):
    try:
        first_result = Mycard.objects.first()
        log.debug(str(first_result.id) + ' ' + first_result.__unicode__())
    except:
        raise Http404
    return render_to_response("hello/index.html",
                              {'first_result': first_result})
