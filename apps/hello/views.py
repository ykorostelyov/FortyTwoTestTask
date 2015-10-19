from django.shortcuts import render_to_response, render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import RequestInfo
from .models import Mycard
import logging
import json
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from forms import MycardForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.models import LogEntry # flake8: noqa
import signals # flake8: noqa

log = logging.getLogger('apps')


# index
def index(request):
    # no data checking
    try:
        first_result = Mycard.objects.first()
        log.debug(str(first_result.id) + ' ' + first_result.__unicode__())
    except:
        raise Http404

    if request.user.is_authenticated():
        current_user_id = request.user.id
        is_auth = True
    else:
        is_auth = False
        current_user_id = 0

    context = {'first_result': first_result,
               'is_auth': is_auth,
               'curr_user': request.user,
               'user_id': current_user_id}
    return render_to_response("hello/index.html", context)


# requests
def requests(request):
    if request.method == "POST":
        pass

    return render(request, 'hello/requests.html')


# new requests  api
def requests_queue(request):

       # TODO On receiving req_id & priority DB upd, order by -id, - priority

    last_10_requests = RequestInfo.objects.order_by("-id").all()[:10]

    # making json array of last 10 records
    requests_array = []
    for curr_request in last_10_requests:
        requests_array.append({
            'id': curr_request.id,
            'priority': curr_request.priority,
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


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/edit/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("You're not the one we were waiting for...")
    else:
        return render_to_response("hello/login.html", {}, context)


@login_required()
# edit
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
