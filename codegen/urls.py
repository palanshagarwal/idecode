from django.conf.urls import patterns, include, url
from codegen import views
urlpatterns = patterns('',
	url(r'^$', views.simple, name='create_code'),
	url(r'^(?P<code_id>[0-9]+)/$', views.update_code, name='update_code'),
    url(r'^clone/(?P<code_id>[0-9]+)/$', views.clone_code, name='clone_code'),
)
