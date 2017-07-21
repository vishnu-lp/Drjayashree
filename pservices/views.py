# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from models import Service, Product
from forms import appointForm


# Create your views here.
def index(request):
    querysetServ = Service.objects.all()
    querysetProd = Product.objects.all()
    context = {
        'servList': querysetServ,
        'prodList': querysetProd,
    }
    return render(request, 'index.html', context)


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


def service_detailed(request, id=None):
    querysetServ = Service.objects.all()
    querysetProd = Product.objects.all()
    instance = get_object_or_404(Service, id=id)

    context = {
        'servList': querysetServ,
        'prodList': querysetProd,
        'title': instance.ServiceTitle,
        'desc': instance.ServiceDescription
    }
    return render(request, 'service_single.html', context)

def product_detailed(request, id=None):
    querysetServ = Service.objects.all()
    querysetProd = Product.objects.all()
    instance = get_object_or_404(Product, id=id)

    context = {
        'servList': querysetServ,
        'prodList': querysetProd,
        'title': instance.ProductTitle,
        'desc': instance.ProductDescription
    }
    return render(request, 'product_single.html', context)

