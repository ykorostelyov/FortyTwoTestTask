from django.shortcuts import render_to_response
from .models import Mycard
import os


PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# list of records
all_result = Mycard.objects.all()
# first record
frst_result = all_result.filter()[:1]


# index
def index(request):
    vars = dict(
        all_result=Mycard.objects.all()
    )
    return render_to_response(os.path.join(BASE_DIR + "/apps/Mydata/templates/Mydata/index.html"),
                              {'frst_result': frst_result})
