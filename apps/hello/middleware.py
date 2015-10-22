__author__ = 'torhammer'

import json
import sys
import models
from django.core.urlresolvers import reverse


class GetRequest(object):
    def process_response(self, request, response):
        try:
            if response['Content-Type'] != 'application/json':
                self.save(request, response)

        except Exception as error:
            # error logging
            print >> sys.stderr, "Error saving request log", error

        return response

    @staticmethod
    def save(request, response):
        meta = request.META.copy()
        # excluding technical requests
        if not (request.path == reverse('requests')
                and request.method == "POST"):
            models.RequestInfo(
                host=request.get_host(),
                path=request.path,
                method=request.method,
                uri=request.build_absolute_uri(),
                status_code=response.status_code,
                remote_addr=meta.pop('REMOTE_ADDR', None),
                is_viewed=False,
                is_ajax=True,
                priority=1
            ).save()
