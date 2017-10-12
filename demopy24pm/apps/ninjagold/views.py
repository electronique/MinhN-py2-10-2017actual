# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(req):
	print req.SESSION["name"]
	return render(req, 'ninjagold/index.html')

def process(req, job):
	print job
	
	req.session["name"] = "Minh"
	# print req.method
	# print req.__dict__
	if req.method == "POST":
		print req.POST["location"]
		return HttpResponse("asfdjlaskjflkasd")
	else:
		return redirect('/gold')
