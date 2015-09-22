from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'hello.views.index', name='home'),
    url(r'^requests/', 'hello.views.requests', name='requests'),
    url(r'^requests_api/', 'hello.views.requests_queue',
        name='requests_api'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^login/$', 'hello.views.user_login', name='login'),
    url(r'^edit/$', 'hello.views.edit', name='edit'),
)
