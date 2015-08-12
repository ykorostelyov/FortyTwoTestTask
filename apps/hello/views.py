from django.shortcuts import render_to_response
from .models import Mycard
import os


PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
# base dir
B_DIR = os.path.dirname(PROJECT_DIR)


# index
def index(request):
    all_result = Mycard.objects.all()
    frst_result = all_result.filter()[:1]
    return render_to_response("hello/index.html", {'frst_result': frst_result})
