from django.shortcuts import render_to_response, render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Mycard, RequestInfo
import logging
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from forms import MycardForm
from django.views.decorators.csrf import csrf_protect
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
        is_auth = True
    else:
        is_auth = False

    context = {'first_result': first_result,
               'is_auth': is_auth}
    return render_to_response("hello/index.html", context)


# requests
@csrf_protect
def requests(request):
    if request.method == "POST":
        if request.is_ajax():
            try:
                request_id = request.POST["request_id"]
                print request_id
                request_priority = request.POST["priority"]
                print request_priority
                RequestInfo.objects.filter(id=request_id)\
                    .update(priority=request_priority)
            except Exception as err:
                log.error(err)
    # GET
    last_10_requests = RequestInfo.objects.order_by("-priority",
                                                    "-id").all()[:10]
    new_requests = RequestInfo.objects.filter(is_viewed=False)

    # marking records as read
    for curr_request in new_requests:
        curr_request.is_viewed = True
        curr_request.save()

    context = {'requests_list': last_10_requests,
               'new_requests_cnt': len(new_requests)}

    return render(request, "hello/requests.html", context)


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
