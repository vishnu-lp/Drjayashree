# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Service,Appointments
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
	list_display = ['ServiceTitle']

admin.site.register(Service,ServiceAdmin)



class AppointmentsAdmin(admin.ModelAdmin):
	list_display = ['Name','ServiceName','Age','timestamp','Booking']

admin.site.register(Appointments,AppointmentsAdmin)