# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Service,Appointments, Product
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
	list_display = ['ServiceTitle']

class ProductAdmin(admin.ModelAdmin):
	list_display = ['ProductTitle']


admin.site.register(Service,ServiceAdmin)
admin.site.register(Product, ProductAdmin)


class AppointmentsAdmin(admin.ModelAdmin):
	list_display = ['Name','ServiceName','Age','timestamp','BookingD','BookingT']

admin.site.register(Appointments,AppointmentsAdmin)