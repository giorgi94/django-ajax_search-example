from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),

	url(r'^admin_log$', views.admin_log, name='admin_log'),

	url(r'^(?P<poster_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<poster_id>[0-9]+)/edit/$', views.edit, name='edit'),

	url(r'^add_video$', views.add_poster, name='addvideo'),

	url(r'^search/$', views.search, name='search'),
]