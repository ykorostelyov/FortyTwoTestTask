from django.contrib import admin
from .models import Mycard, RequestInfo
from django.contrib.admin.models import LogEntry


admin.site.register(Mycard)
admin.site.register(RequestInfo)
admin.site.register(LogEntry)
