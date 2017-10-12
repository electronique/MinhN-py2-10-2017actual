# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(req):
	return HttpResponse("hello world")

def display_form(req):
	return render(req, 'surveyform/index.html')

def process(req):
	print req.__dict__
	if req.method == "POST":
		req.session["first_name"] = req.POST["first_name"]
		req.session["last_name"] = req.POST["last_name"]
		req.session["language"] = req.POST["language"]
		print req.POST["first_name"]
		print req.POST["last_name"]
		print req.POST["language"]
		url = "/survey/display_data/{}/{}/{}".format(req.POST["first_name"],req.POST["last_name"], req.POST["language"])
	return redirect(url)

def display_data(req, first_name, last_name, location):
	print first_name
	print last_name
	print location
	context = {
		"fname":req.session["first_name"],
		"lname":req.session["last_name"],
		"favorite_language":req.session["language"],
		"students":["angela", "jenna", "manju", "david"]
	}
	print req.session
	return render(req, "surveyform/form_data.html", context)