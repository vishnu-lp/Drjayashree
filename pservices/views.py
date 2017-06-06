# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Service, Product
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