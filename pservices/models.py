# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.



class Service(models.Model):
    ServiceTitle = models.CharField(max_length=200, db_index=True)
    ServiceDescription = models.TextField(max_length=10000, db_index=True)
    ServiceImage = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.ServiceTitle


class Product(models.Model):
    ProductTitle = models.CharField(max_length=200, db_index=True)
    ProductDescription = models.TextField(max_length=10000, db_index=True)
    ProductImage = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.ProductTitle


class Appointments(models.Model):
    Name = models.CharField(max_length=100, db_index=True)
    ServiceName = models.ForeignKey(Service)
    Age = models.IntegerField(blank=True)
    BookingD = models.DateField(default="2017-01-01")
    BookingT = models.TimeField(default="00:00:00")
    Description = models.TextField(blank=True)
    timestamp = models.DateField(auto_now_add=True, blank=True)
