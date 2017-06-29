from django.conf.urls import url, include
from .views import *


urlpatterns = [
	url(r'^$', loggedIn, name = 'all'),
	url(r'^delete/(\d+)/', delete, name = 'delete'),
	url(r'^search_query/$', search),
	url(r'^update/(\d+)/$', update, name = 'update'),
	url(r'^add/$', add, name = 'add'),
	url(r'^view/(\d+)/$', view, name = 'view'),

]