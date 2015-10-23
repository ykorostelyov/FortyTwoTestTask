from django.contrib import admin
from .models import Mycard, RequestInfo, EventLog


admin.site.register(Mycard)
admin.site.register(RequestInfo)
admin.site.register(EventLog)
