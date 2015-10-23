from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^', include('apps.hello.urls')),
    url(r'^admin/', include(admin.site.urls), name='django-admin'),

    (r'^uploads/(?P<path>.*)$',
     'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT})
)

urlpatterns += staticfiles_urlpatterns()
