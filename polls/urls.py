from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',
	url(r'^$', index, name='index'),
	url(r'^specifics/(?P<poll_id>\d+)/$', detail, name='detail'),	
	url(r'^(?P<poll_id>\d+)/results/', results, name='results'),
	url(r'^(?P<poll_id>\d+)/vote/', vote, name='vote'),
)