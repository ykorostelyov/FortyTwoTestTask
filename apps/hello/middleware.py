__author__ = 'torhammer'

import json
import sys
import models


def dumps(value):
    return json.dumps(value, default=lambda o: None)


class GetRequest(object):
    def process_response(self, request, response):
        try:
            self.save(request, response)
        except Exception as error:
            print >> sys.stderr, "Error saving request log", error

        return response

    @staticmethod
    def save(request, response):
        meta = request.META.copy()
        meta.pop('QUERY_STRING', None)
        meta.pop('HTTP_COOKIE', None)
        models.RequestInfo(
            host=request.get_host(),
            path=request.path,
            method=request.method,
            uri=request.build_absolute_uri(),
            status_code=response.status_code,
            user_agent=meta.pop('HTTP_USER_AGENT', None),
            remote_addr=meta.pop('REMOTE_ADDR', None),
            is_ajax=request.is_ajax(),
            is_viewed=False
        ).save()
