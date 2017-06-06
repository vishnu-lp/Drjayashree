# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Service, Product
from forms import appointForm
# Create your views here.
def index(request):
    querysetServ=Service.objects.all()
    querysetProd=Product.objects.all()
    context={
        'servList':querysetServ,
        'prodList':querysetProd,
    }
    return render(request, 'index.html',context )

def about(request):
    querysetServ = Service.objects.all()
    querysetProd = Product.objects.all()
    context = {
        'servList': querysetServ,
        'prodList': querysetProd,
    }
    return render(request, 'aboutus.html', context)

def contact(request):
    querysetServ = Service.objects.all()
    querysetProd = Product.objects.all()
    context = {
        'servList': querysetServ,
        'prodList': querysetProd,
    }
    return render(request, 'contactus.html', context)

def appoint(request):
    form = appointForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('appointments')

    context = {
        "form": form
    }

    return render(request, 'appointments.html', context)
