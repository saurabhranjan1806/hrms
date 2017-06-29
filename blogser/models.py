# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models  import User
from django.db import models

# Create your models here.

class education(models.Model):
	Education = models.CharField(max_length=30)
	Date = models.DateTimeField(auto_now = True)
	Grade = models.CharField(max_length=1)
	Remark = models.CharField(max_length=30)
	School = models.CharField(max_length=30)

	def __unicode__(self):
		return self.Education

class hrms(models.Model):
	EmployeeNo = models.AutoField(primary_key=True)
	FirstName = models.CharField(max_length=15)
	LastName = models.CharField(max_length=15)
	CurrentTime = models.DateTimeField(auto_now=True)
	Address = models.TextField()
	MaritalStatus = models.CharField(max_length=15)
	GradeEmployee = models.CharField(max_length=10)
	HigestEducation = models.ForeignKey(education)
	# SecondaryEducation = models.ForeignKey(education)
	# OtherEducation = models.ForeignKey(education)

	def __unicode__(self):
		return self.FirstName


