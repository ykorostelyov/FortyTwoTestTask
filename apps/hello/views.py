from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponse
from .models import RequestInfo
from .models import Mycard
import logging
import json


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


# requests
def requests(request):
    return render(request, 'hello/requests.html')


# new requests  api
def requests_queue(request):

    last_10_requests = RequestInfo.objects.order_by("-id").all()[:10]

    # making json array of last 10 records
    requests_array = []
    for curr_request in last_10_requests:
        requests_array.append({
            'id': curr_request.id,
            'method': curr_request.method,
            'uri': curr_request.uri,
            'status_code': curr_request.status_code,
            'remote_addr': curr_request.remote_addr,
        })
    new_requests = RequestInfo.objects.filter(is_viewed=False)

    # marking records as read
    for curr_request in new_requests:
        curr_request.is_viewed = True
        curr_request.save()

    context = {'last_10_requests': requests_array,
               'new_requests_cnt': len(new_requests)}
    return HttpResponse(json.dumps(context),
                        content_type="application/json")
