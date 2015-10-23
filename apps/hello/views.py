from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import Mycard, RequestInfo
import logging
from forms import MycardForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
import json
import signals # flake8: noqa


log = logging.getLogger('apps')


def index(request):
    my_data = Mycard.objects.first()
    context = {'my_data': my_data}
    return render(request, "hello/index.html", context)


@csrf_protect
def requests(request):
    if request.method == "POST":
        if request.is_ajax():
            try:
                request_id = request.POST["request_id"]
                request_priority = request.POST["priority"]
                RequestInfo.objects.filter(id=request_id)\
                    .update(priority=request_priority)
            except Exception as err:
                log.error(err)
    # GET
    last_10_requests = RequestInfo.objects.order_by("-priority",
                                                    "-id").all()[:10]
    new_requests = RequestInfo.objects.filter(is_viewed=False)
    RequestInfo.objects.filter(priority=1).update(priority=0)
    # marking records as read
    for curr_request in new_requests:
        curr_request.is_viewed = True
        curr_request.save()

    context = {'requests_list': last_10_requests,
               'new_requests_cnt': len(new_requests)}

    return render(request, "hello/requests.html", context)


# checking of new data
def requests_api(request):
    new_requests = RequestInfo.objects.filter(is_viewed=False)
    return HttpResponse(json.dumps({'new_requests_cnt': len(new_requests)}),
                        content_type="application/json")


@login_required()
def edit(request):
    # no data checking
    try:
        edit_form = MycardForm(instance=Mycard.objects.first())
    except:
        raise Http404
    if request.method == 'POST':
        edit_form = MycardForm(request.POST, request.FILES,
                               instance=Mycard.objects.first())
        if edit_form.is_valid():
            edit_form.save()

            if request.is_ajax():
                return HttpResponse("OK")
            else:
                return redirect('/')
        else:
            return HttpResponse(str(edit_form))

    context = {'edit_form': edit_form}
    return render(request, "hello/edit.html", context)
