from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Mycard
from .models import RequestInfo
import os


PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
# base dir
B_DIR = os.path.dirname(PROJECT_DIR)


# index
def index(request):
    full_path = os.path.join(B_DIR+"/apps/Mydata/templates/Mydata/index.html")
    all_result = Mycard.objects.all()
    frst_result = all_result.filter()[:1]
    return render_to_response(full_path, {'frst_result': frst_result})
