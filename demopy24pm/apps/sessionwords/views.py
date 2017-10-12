# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(req):
	class Person(object):
		def __init__(self, name, age):
			self.name = name
			self.age = age 

	person = Person("minh", 24)
	context = {
		"person":person
	}
	return render(req, "sessionwords/index.html", context)