from django.shortcuts import render_to_response
from .models import Mycard
import logging


log = logging.getLogger('apps')


# index
def index(request):
    first_result = Mycard.objects.order_by('id')[0]
    return render_to_response("hello/index.html",
                              {'first_result': first_result})
