from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponse
from .models import RequestInfo
from .models import Mycard
import logging
import json


log = logging.getLogger('apps')


# index
def index(request):
    try:
        first_result = Mycard.objects.first()
        log.debug(str(first_result.id) + ' ' + first_result.__unicode__())
    except:
        raise Http404
    context = {'first_result': first_result}
    return render_to_response("hello/index.html", context)


def requests(request):
    return render(request, 'hello/requests.html')


def requests_queue(request):
    if 'last_request' in request.GET:
        last_request = request.GET['rec_id']
        last_10_requests = RequestInfo.objects.exclude(id=last_request)\
                                      .order_by("-id").all()[:10]
    else:
        last_10_requests = RequestInfo.objects.order_by("-id").all()[:10]

    new_requests = RequestInfo.objects.filter(is_viewed=False)

    requests_array = []
    for curr_request in last_10_requests:
        requests_array.append({
            'id': curr_request.id,
            # 'date': curr_request.date,
            'method': curr_request.method,
            'uri': curr_request.uri,
            'status_code': curr_request.status_code,
            'remote_addr': curr_request.remote_addr,
            # 'timestamp': curr_request.timestamp.isoformat(),
        })

    for curr_request in new_requests:
        curr_request.is_viewed = True
        curr_request.save()

    context = {'last_10_requests': requests_array, 'new_requests_cnt': len(
        new_requests)}

    return HttpResponse(json.dumps(context),
                        content_type="application/json")
