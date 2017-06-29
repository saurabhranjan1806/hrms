# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import auth
from django.shortcuts import render
from django.http import *
from django.contrib.auth.models  import User
from .forms import *
from .models import *
from django.db.models import *
# Create your views here.

def loggedIn(request):
	n = hrms.objects.all()
	return render(request,'blogser/home.html',{'fullname':request.user.username, 't':n})

def add(request):
	if request.user.is_authenticated():
		if request.method=="POST":
			form = hrmsForm(request.POST)
			if form.is_valid:
				form.save()
				return HttpResponseRedirect('/loggedIn/')
		else:
			form = hrmsForm()
		return render(request,'blogser/add.html',{'fullname':request.user.username, 'form': form})
	else:
		return HttpResponseRedirect('/')

def view(request, d):
	n = hrms.objects.get(EmployeeNo = d)
	return render(request,'blogser/view.html',{'fullname':request.user.username, 'i':n})


def delete(request,d):
    n = hrms.objects.get(EmployeeNo= d)
    n.delete()
    return HttpResponseRedirect('/loggedIn/')


def search(request):
	if request.method == 'POST':
		squery = request.POST['search_box']
		if squery:
			s = hrms.objects.filter(Q(FirstName__icontains=squery)|Q(LastName__icontains=squery))
			if s:
				return render(request,'blogser/home.html',{'fullname':request.user.username,'t':s})
        	else:
        		return render(request,'blogser/home.html')
       	else:
       		return HttpResponseRedirect('/logged_in/')

def update(request, id):
	n = hrms.objects.get(EmployeeNo = id)
	if request.method == "POST":
		form = hrmsForm(request.POST,instance=n)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/loggedIn/')
	else:
		form = hrmsForm(instance=n)
	return render(request,'blogser/add.html',{'fullname':request.user.username, 'form': form})