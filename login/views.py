# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import auth
from django.shortcuts import render
from django.http import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User

# Create your views here.

def index(request):
	form = UserCreationForm()
	return render(request, 'login/home.html', {'form' : form})


def auth_view(request):
	username = request.POST['username']
	password = request.POST['password']
	try:
		user = auth.authenticate(username=username, password=password)
		auth.login(request, user)
	except:
		return HttpResponseRedirect('/invalid/')
	return HttpResponseRedirect('/loggedIn/')


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')


def register(request):
	if request.method=="POST":
		form = UserCreationForm(request.POST)
		if form.is_valid:
			form.save()
			return render(request, 'login/register_success.html', {'name': request.POST['username']})
	# else:
	# 	form = UserCreationForm()
	# return render(request, 'login/register.html', {'form':form})


# def loggedIn(request):
#     if request.user.is_authenticated():
#         return render(request,'login/login.html',{'fullname':request.user.username})
#     else:
#         return HttpResponseRedirect('/')