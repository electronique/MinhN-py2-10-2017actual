from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^\d+', views.number),
	url(r'^\w+', views.index)	
]