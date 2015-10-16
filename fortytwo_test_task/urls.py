from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'hello.views.index', name='home'),
    url(r'^requests/', 'hello.views.requests', name='requests'),
    url(r'^requests_api/', 'hello.views.requests_queue',
        name='requests_api'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    (r'^accounts/login/$',  login),
    url(r'^logout/$', logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^edit/$', 'hello.views.edit', name='edit'),
    url(r'^uploads/$', 'hello.views.edit', name='uploads'),
    url(r'^accounts/profile/$', 'hello.views.index', name='home'),
)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^uploads/(?P<path>.*)$',
                             'django.views.static.serve',
                             {'document_root': settings.MEDIA_ROOT}))
