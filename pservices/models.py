# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Service(models.Model):
	ServiceTitle = models.CharField(max_length=200,db_index=True)
	ServiceDescription = models.TextField(max_length=500,db_index=True)


	def __str__(self):
		return self.ServiceTitle



class Appointments(models.Model):
	Name = models.CharField(max_length=100,db_index=True)
	ServiceName = models.ForeignKey(Service)
	Age = models.IntegerField()	
	Booking = models.DateTimeField()	
	timestamp = models.DateField(auto_now_add=True)

