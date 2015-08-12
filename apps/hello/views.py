from django.shortcuts import render_to_response
from .models import Mycard


def index(request):
    all_result = Mycard.objects.all()
    frst_result = all_result.filter()[:1]
    return render_to_response("hello/index.html", {'frst_result': frst_result})
