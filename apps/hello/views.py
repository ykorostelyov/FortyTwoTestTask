from django.shortcuts import render_to_response
from django.http import Http404
from .models import Mycard
import logging


log = logging.getLogger('apps')


# index
def index(request):
    # no data checking
    try:
        first_result = Mycard.objects.first()
        log.debug(str(first_result.id) + ' ' + first_result.__unicode__())
    except:
        raise Http404

    context = {'first_result': first_result}
    return render_to_response("hello/index.html", context)
