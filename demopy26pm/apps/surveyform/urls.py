from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^form$', views.display_form),
	url(r'^process$', views.process),
	url(r'^display_data/(?P<first_name>\w+)/(?P<last_name>\w+)/(?P<location>\w+)$', views.display_data)	
]