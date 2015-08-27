from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from .models import Mycard
import logging


log = logging.getLogger('apps')


# index
def index(request):
    first_result = get_object_or_404(Mycard, pk=1)

    log.debug(str(first_result.id) + ' ' + first_result.__unicode__())

    return render_to_response("hello/index.html",
                              {'first_result': first_result})
