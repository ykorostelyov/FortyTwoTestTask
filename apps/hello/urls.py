from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(
    '',
    url(r'^$', 'hello.views.index', name='home'),
    url(r'^requests/', 'hello.views.requests', name='requests'),
    url(r'^requests_cnt/', 'hello.views.requests_cnt', name='requests_cnt'),
    url(r'^edit/$', 'hello.views.edit', name='edit'),
    url(r'^uploads/$', 'hello.views.edit', name='uploads'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^accounts/login/$',  login, name='login'),
    url(r'^logout/$', logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^accounts/profile/$', 'hello.views.index', name='home'),
)

urlpatterns += staticfiles_urlpatterns()
