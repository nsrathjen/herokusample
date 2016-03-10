from django.conf.urls import patterns, url

urlpatterns = patterns('photoupload.views',
    url(r'^list/$', 'list_pictures', name='list'),
)